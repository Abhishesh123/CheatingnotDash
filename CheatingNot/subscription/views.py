from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userprofile.mixins import AuthUserMixin
from subscription.models import *
import uuid
from subscription.serializers import *
from userprofile.models import *
from threading import Timer
from subscription import Checksum
    
    
class AllPlans(AuthUserMixin,APIView):

    def get(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        plan = Plans.objects.exclude(id=1)
        serializer = PlanSerializer(plan, many=True)
        return Response({'status':True,'data':serializer.data})
    

class UserSubscription(AuthUserMixin,APIView):
    def get(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user = resp['user']
        plan = UserDailyDose.objects.get(user=user)
        serializer = UserDoseSerializer(plan)
        return Response({'status':True,'data':serializer.data})   
    
def get_paid_plan_amount(user,data):
    order_id = 'CheatingNot_plan_'+str(uuid.uuid4().hex)[:10]
    
    plan_detail = PlanDetails.objects.get(pk=data['plan_id'])
    plan_price          = float(plan_detail.price) 
    wallet_percentage   = plan_detail.wallet_percentage  
    discount_percentage = plan_detail.discount_percentage 
    
    wallet = Wallet.objects.get(user=user)
    w_amount = float(wallet.wallet_amount)
    if w_amount > 0 and wallet_percentage > 0:
        wallet_amount_used = float(w_amount) * (wallet_percentage/100)                    
    else:
        wallet_amount_used = 0
     
    if discount_percentage > 0: 
        discount_amount    = plan_price * (discount_percentage/100)  
    else:
        discount_amount = 0
    paytm_amount = plan_price - (wallet_amount_used+discount_amount)  
    
    cashback_percentage = Discount.objects.get(id=1).cashback_percentage
    if cashback_percentage > 0:
        cashback_amount = plan_price*(cashback_percentage/100)
    else:
        cashback_amount = 0

        
    pr = PurchaseRequest.objects.create(user=user,plan_id=plan_detail.id,plan_name=plan_detail.plan.name)
    pr.order_id     = order_id
    pr.wallet_amount     = wallet_amount_used
    pr.discount_amount   = discount_amount
    pr.paytm_amount      = paytm_amount
    pr.plan_price_amount = plan_price
    pr.save()
    resp_json = {
        'order_id':order_id,
        'total_amount':plan_price,
        'discount_amount':discount_amount,
        'wallet_amount':wallet_amount_used,
        'paytm_amount':paytm_amount,
        'status_code':200,
        'cashback_amount':cashback_amount,
        'msg':'payment request generated successfully'
    }
    return resp_json
    
Discount = ''

def get_paid_accessories_amount(user,data):
    order_id = 'CheatingNot_accessories_'+str(uuid.uuid4().hex)[:10]
    accessories_detail = AccessoriesDetails.objects.get(pk=data['accessories_id']) 
    accessories_price   = float(accessories_detail.price )
    wallet_percentage   = accessories_detail.wallet_percentage  
    discount_percentage = accessories_detail.discount_percentage 
    
    wallet = Wallet.objects.get(user=user)
    w_amount = float(wallet.wallet_amount)
    if w_amount > 0 and wallet_percentage > 0:
        wallet_amount_used = w_amount * (wallet_percentage/100)                    
    else:
        wallet_amount_used = 0
    if discount_percentage > 0:
        discount_amount    = accessories_price * (discount_percentage/100)
    else:
        discount_amount = 0
    
    paytm_amount = accessories_price - (wallet_amount_used+discount_amount)  
            
    cashback_percentage = Discount.objects.get(id=1).cashback_percentage
    if cashback_percentage > 0:
        cashback_amount = accessories_price*(cashback_percentage/100)
    else:
        cashback_amount = 0
       
    pr = PurchaseRequest.objects.create(user=user,accessories_id=accessories_detail.id,accessories_name=accessories_detail.accessories.name)
    pr.order_id     = order_id
    pr.wallet_amount     = wallet_amount_used
    pr.discount_amount   = discount_amount
    pr.paytm_amount      = paytm_amount
    pr.plan_price_amount = accessories_price
    pr.save()
    resp_json = {
        'order_id':order_id,
        'total_amount':accessories_price,
        'discount_amount':discount_amount,
        'wallet_amount':wallet_amount_used,
        'paytm_amount':paytm_amount,
        'status_code':200,
        'cashback_amount':cashback_amount,
        'msg':'payment request generated successfully'
    }
    return resp_json
    
    
class GetPaidAmount(AuthUserMixin, APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.headers)
        if not resp['status']:
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        user = resp['user']
        """ paid amount for  plan """
        pid = data['plan_id']
        if pid:
            if UserDailyDose.objects.filter(user_id=user.id,plan_id=pid,plan_expire_at__lt=datetime.today()).exists():
                return Response({'status_code':208,'msg':'Plan already Subscribed'},status=status.HTTP_208_ALREADY_REPORTED)
            resp = get_paid_plan_amount(user,data)
            return Response(resp)
        elif data['accessories_id']:
            """ paid amount for  accessories """
            resp = get_paid_accessories_amount(user,data)
            return Response(resp)
        
        
def update_plan_purched_by_user(user,data):
    p = PlanPurchedByUser.objects.create(user=user)
    plan_purchase = PurchaseRequest.objects.get(order_id=data['order_id'])
    p.plan_id       = data['plan_id']
    p.plan_name     = data['plan_name']
    p.paytm_txn_id  = data['txn_id']
    p.order_id      = data['order_id']
    
    p.paytm_amount      = plan_purchase.paytm_amount
    p.cashback_amount   = plan_purchase.cashback_amount
    p.discount_amount   = plan_purchase.discount_amount
    p.wallet_amount     = plan_purchase.wallet_amount
    p.plan_price_amount = plan_purchase.plan_price_amount
    p.save()
    
def update_accessories_purched_by_user(user,data):
    p = PlanPurchedByUser.objects.create(user=user)
    plan_purchase = PurchaseRequest.objects.get(order_id=data['order_id'])
    
    p.accessories_id       = data['accessories_id']
    p.plan_name            = data['plan_name']
    p.paytm_txn_id         = data['txn_id']
    p.order_id             = data['order_id']
    
    p.paytm_amount      = plan_purchase.paytm_amount
    p.cashback_amount   = plan_purchase.cashback_amount
    p.discount_amount   = plan_purchase.discount_amount
    p.wallet_amount     = plan_purchase.wallet_amount
    p.plan_price_amount = plan_purchase.plan_price_amount
    p.save()
    
import json
import requests

def txn_status(order_id):
    url = "https://securegw.paytm.in/order/status" #for staging
    
    paytmParams = dict()
    paytmParams["MID"] = "iICDco50887813089239" 
    paytmParams["ORDERID"] = order_id
    checksum = Checksum.generate_checksum(paytmParams, "1GAcDK_u@TPXqybg")
    paytmParams["CHECKSUMHASH"] = checksum
    post_data = json.dumps(paytmParams)
    
    response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"})
    data=response.json()
    status_resp = json.dumps(data)
    print(status_resp)
    PaytmPaymentStatus.objects.create(**data)
    return None
        
        
class EnrollUserSubscription(AuthUserMixin, APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.headers)
        if not resp['status']:
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
        user = resp['user']
        if data['txn_status'] == 'True':
            plan_details = PlanDetails.objects.get(plan_id=data['plan_id'])
            data.update({'plan_name':plan_details.name})
            userdose = UserDailyDose.objects.get(user_id=user.id)
            userdose.plan_name            = plan_details.name
            userdose.remaining_hi         = int(userdose.remaining_hi)         + int(plan_details.hi)
            userdose.remaining_boosts     = int(userdose.remaining_boosts)     + int(plan_details.boosts)
            userdose.remaining_hearts     = int(userdose.remaining_hearts)     + int(plan_details.hearts)
            userdose.remaining_talktime   = int(userdose.remaining_talktime)   + int(plan_details.talktime)
            userdose.remaining_superlikes = int(userdose.remaining_superlikes) + int(plan_details.superlike)
            userdose.order_id             = data['order_id']
            userdose.is_active            = True
            userdose.is_expired           = False
            userdose.plan_expire_at       = datetime.now() + timedelta(days=int(plan_details.validity))
            userdose.save()
            update_plan_purched_by_user(user,data)
            
        else:
            return Response({'status_code':404,'msg':'Plan Purchased failed'}, status=status.HTTP_400_BAD_REQUEST)
            
        


            
class EnrollUserAccessories(AuthUserMixin, APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.headers)
        if not resp['status']:
            return Response(resp)
        user = resp['user']
        if data['payment_status']:
            accessories = AccessoriesDetails.objects.get(accessories_id=data['accessories_id'])
            userdose = UserDailyDose.objects.get(user_id=user.id)
            userdose.remaining_hi          = int(userdose.remaining_hi)         + int(accessories.hi)
            userdose.remaining_boosts      = int(userdose.remaining_boosts)     + int(accessories.boosts)
            userdose.remaining_hearts      = int(userdose.remaining_hearts)     + int(accessories.hearts)
            userdose.remaining_talktime    = int(userdose.remaining_talktime)   + int(accessories.talktime)
            userdose.remaining_superlikes  = int(userdose.remaining_superlikes) + int(accessories.superlike)
            userdose.save()
            update_accessories_purched_by_user(user,data)
        else:
            return Response({'status_code':404,'msg':'Plan Purchased failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        
def finshboost():
    pass
        
class StartBoost(APIView):
    def get(self, request, user_id):
        try:
            user = Users.objects.get(user_id=user_id)
            user_dose = UserDailyDose.objects.get(user_id=user_id)
        except Exception as e:
            return Response({'status': False, 'message': 'No user found'})

        if  int(user_dose.remaining_boosts) > 0:
            user_dose.remaining_boosts = int(user_dose.remaining_boosts)-1
            user_dose.save()
            user.is_boost = True
            user.priority = datetime.now().timestamp()
            user.save()
            t = Timer(1800.00, finshboost, args=[user.pk])  # duration in second
            t.start()
            return Response({'status': True, 'message': 'your boost is started now'})
        elif user_dose.is_expired == False and int(user_dose.remaining_boosts) >= 0:
            return Response({'status': True, 'message': 'You already boosted your profile'})
        elif int(user_dose.remaining_boosts) >= 0:
            return Response({'status': True, 'message': 'sorry you did not have any boost'})
        


         
#         