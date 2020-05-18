from django.shortcuts import render,redirect
import datetime
from django.contrib.sessions.models import Session
from userprofile.models import Users,Match,Reports
from subscription.models import PlanPurchedByUser,PaytmPaymentStatus,PurchaseRequest,Accessories,AccessoriesDetails,Wallet,UserDailyDose
from django.utils import timezone
from dashboard.forms import  userForm
from django.db.models import Sum,Count
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def Index(request):
	today = datetime.date.today()
	todayusers = Users.objects.filter(create_at__date = today).count()
	totaluser = Users.objects.all().count()
	todayMatch = Match.objects.filter(create_at__date = today).count()
	totalMatch = Match.objects.all().count()
	todaysales = PlanPurchedByUser.objects.filter(plan_purched_at__date = today).aggregate(total_plan_price_amount = Sum('plan_price_amount'))
	totalsales = PlanPurchedByUser.objects.aggregate(total_plan_price_amount = Sum('plan_price_amount'))
	totalPlus=PlanPurchedByUser.objects.filter(plan_name__startswith="Plus").count()
	totalSuper=PlanPurchedByUser.objects.filter(plan_name__startswith="Super").count()
	
    
	return render(request,'homepage.html',{
	'todayuser':todayusers,
	'totaluser':totaluser,
    'todaysale':todaysales,
    'totalsale':totalsales,
    'todayMatchs':todayMatch,
    'totalMatchs':totalMatch,
    'totalPluss':totalPlus,
    'totalSupers':totalSuper

	})

def Login(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username = username, password=  password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request, 'homepage.html')
        else:
            return HttpResponse("Invalid login details..")
    else:
        return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('/')
def userList(request):
    user = Users.objects.filter(active = True)
    page = request.GET.get('page', 1)
    paginator = Paginator(user, 2)
    try:
        userlists = paginator.page(page)

    except PageNotAnInteger:
        userlists = paginator.page(1)
    except EmptyPage:
        userlists = paginator.page(page.num_pages)
    
    return render(request, 'userlisting.html', {'users':user,'userlists':userlists})
def Detailsuser(request, id):
    user = Users.objects.get(id = id)
    print(user)
    return render(request, 'detailsuser.html', {'user': user})

def userUpdate(request, id):
    obj = Users.objects.get(pk = id)    
    form = userForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/userlist')   
    return render(request, 'userupdate.html', {'form': obj})

def blockuser(request, id):
    user = Users.objects.get(pk = id)
    user.active = False
    user.save()
    return redirect('/userList')
def unblockuser(request, id):
    user = Users.objects.get(pk = id)
    user.active = True
    user.save()
    return redirect('/unblockuser')

def blockUserslist(request):
    user = Users.objects.filter(active = False)
    page = request.GET.get('page', 1)
    paginator = Paginator(user, 2)
    try:
        blocks = paginator.page(page)

    except PageNotAnInteger:
        blocks = paginator.page(1)
    except EmptyPage:
        blocks = paginator.page(page.num_pages)
    return render(request, 'blockuserlist.html', {'users':user,'blocks':blocks})

def searchUser(request):
    if request.method == 'POST':
        data = request.POST['q']
        # data = request.POST['datejoined']
        print(data)
        user  = Users.objects.filter(dob__icontains= data) or Users.objects.filter(phone_no__icontains= data) or Users.objects.filter(email__icontains= data) or Users.objects.filter(gender__icontains= data) or Users.objects.filter(id__icontains= data)

        return render(request, 'userlisting.html', {'users':user})
def planpurchedbyuser(request):
    PlanPurchedBy = PlanPurchedByUser.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(PlanPurchedBy, 2)
    try:
        subs = paginator.page(page)

    except PageNotAnInteger:
        subs = paginator.page(1)
    except EmptyPage:
        subs = paginator.page(page.num_pages)
    
    return render(request, 'userSubscriptions.html', 
        {'PlanPurchedByuser':PlanPurchedBy,
        'subs':subs}
        )

def planpurchedbyuserDetails(request, id):
    user = PlanPurchedByUser.objects.get(id = id)
  
    return render(request, 'userSubscriptionDetails.html', 
        {'planpurchedbyUserDetail':user}
        )
def matchedprofiles(request):
    matchpro=Match.objects.all()
    return render(request, 'matched.html', {'users':matchpro})
def Matchprofiles(request, id):
    matcheddel = Match.objects.get(id = id)
    matcheddel.delete()
    return redirect('/matchedprofiles')
def Reported(request):
    Report=Reports.objects.all()
    return render(request,'report.html',{'Reports':Report})
def deleteReported(request, id):
    Reporteddel = Reports.objects.get(id = id)
    Reporteddel.delete()
    return redirect('/Reported')
def paytmpaymentStatus(request):
    PaytmPayment=PaytmPaymentStatus.objects.all()
    return render(request,'paymentstatus.html',
        {'paytmpayment':PaytmPayment}
        )

def Paymentdetail(request, id):
    user = PaytmPaymentStatus.objects.get(id = id)
    return render(request, 'paymentdetails.html', {'user': user})
def ordermanagement(request):
    order=PurchaseRequest.objects.all()
    return render(request, 'ordermanage.html', {'order':order})
def ordermanagementDetails(request, id):
    user = PurchaseRequest.objects.get(id = id)
   
    return render(request, 'orderdetails.html', 
        {'planpurchedbyUserDetail':user}
        )

def userListCSV(request):

    # Get all data from UserDetail Databse Table
    users = Users.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="userlist.csv"'

    writer = csv.writer(response)
    writer.writerow(['User ID', 'Username', 'Phone', 'DOB','Created Date'])

    for user in users:
        writer.writerow([user.id, user.user,  user.phone_no,user.dob,user.create_at])

    return response
def datefilter(request):
    if request.method == 'POST':
        data = request.POST['start']
        print(data)
        user  = Users.objects.filter(create_at__icontains= data)  

        return render(request, 'userlisting.html', {'users':user})
def Access(request):
    return render(request,'addacess.html')

def AddAccessories(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('accessories')and request.POST.get('is_active'):
                accessories=Accessories()
                accessories.name= request.POST.get('name')
                print(accessories.name)
                accessories.accessories= request.POST.get('accessories')
                accessories.is_active= request.POST.get('is_active')
                accessories.save()
                
                return render(request,'addacess.html')  

            else:
                return render(request,'addacess.html')
def DetailsAccessories(request):
    return render(request,'DetailsAccessories.html')

def AddAccessoriesdetails(request):
    if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('price') and request.POST.get('validity') and request.POST.get('Description') and request.POST.get('remaining_hi') and request.POST.get('remaining_hearts') and request.POST.get('remaining_boosts') and request.POST.get('remaining_talktime') and request.POST.get('remaining_superlikes') and request.POST.get('wallet_percentage') and request.POST.get('discount_percentage'):
                accessories=AccessoriesDetails()
                accessories.name= request.POST.get('name')
                accessories.accessories= request.POST.get('price')
                accessories.is_active= request.POST.get('validity')
                accessories.accessories= request.POST.get('Description')
                accessories.is_active= request.POST.get('remaining_hi')
                accessories.accessories= request.POST.get('remaining_hearts')
                accessories.is_active= request.POST.get('remaining_boosts')
                accessories.accessories= request.POST.get('remaining_boosts')
                accessories.is_active= request.POST.get('remaining_talktime')
                accessories.is_active= request.POST.get('remaining_superlikes')
                accessories.is_active= request.POST.get('wallet_percentage')
                accessories.is_active= request.POST.get('discount_percentage')
                accessories.save()
                
                return render(request,'DetailsAccessories.html')  

            else:
                return render(request,'DetailsAccessories.html')


def userAnalytics(request):
    labelpro = []
    datapro = []
    
    UserProfiles = Users.objects.filter(create_at__lte=datetime.datetime.today(), create_at__gt=datetime.datetime.today()-datetime.timedelta(days=30)).\
    values('create_at__month').annotate(count=Count('id'))
    for usersdatapro in UserProfiles:
        labelpro.append(usersdatapro['create_at__month'])
        datapro.append(usersdatapro['count'])
        prosdata={
            "plabels":labelpro,
            "pdata":datapro
        }
        print(prosdata)
    print(UserProfiles)
    
   
    return render(request,'useranalytics.html',{'prosdatas':prosdata})
def subsAnalytics(request):
    labelss = []
    datas = []
    PurchaseRequests=PlanPurchedByUser.objects.values('order_id').annotate(paytm_amount=Sum('paytm_amount'))

    for Purchase in PurchaseRequests:
        labelss.append(Purchase['order_id'])
        datas.append(Purchase['paytm_amount'])
        data={
            "ulabels":labelss,
            "udata":datas
        }
        print(data)
    return render(request,'subsanalytics.html',{'datas':data})

def orderAnalytics(request):
    labelss = []
    datas = []
    PurchaseRequests=PurchaseRequest.objects.values('order_id').annotate(paytm_amount=Sum('paytm_amount'))

    for Purchase in PurchaseRequests:
        labelss.append(Purchase['order_id'])
        datas.append(Purchase['paytm_amount'])
        data={
            "ulabels":labelss,
            "udata":datas
        }
        print(data)
    return render(request,'orderanayltics.html',{'datas':data})

def searchOrder(request):
    if request.method == 'POST':
        data = request.POST['search']
        # data = request.POST['datejoined']
        order  = PurchaseRequest.objects.filter(order_id__icontains= data) or PurchaseRequest.objects.filter(plan_id__icontains= data) 

        return render(request, 'ordermanage.html', {'users':order})

def OrderCSV(request):

    # Get all data from UserDetail Databse Table
    orders = PurchaseRequest.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="order.csv"'

    writer = csv.writer(response)
    writer.writerow(['User ID', 'Username', 'Plan Id', 'Plan Name','Accessories Id','Accessories Name','Order Id','Paytm Amount','Cashback Amount','Discount Amount','Wallet Amount','Plan Price Amount','Plan Request At'])

    for order in orders:
        writer.writerow([order.id, order.user,order.plan_id,order.plan_name,order.accessories_id,order.accessories_name,order.order_id,order.paytm_amount,order.cashback_amount,order.discount_amount,order.wallet_amount,order.plan_price_amount,order.plan_request_at])

    return response

def wallet(request):
    walltes=Wallet.objects.all()
    return render(request,'wallet.html',{'walltes':walltes})
def UserdailyDose(request):
    UserDaily=UserDailyDose.objects.all()
    return render(request,'userdailydose.html',{'userdailydose':UserDaily})

def Userdailydosedetail(request,id):

    Userdose=UserDailyDose.objects.get(id = id)
    print(Userdose)
    return render(request, 'userdosedetails.html', {'Userdose': Userdose})

