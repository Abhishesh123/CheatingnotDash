from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.http import JsonResponse


from userprofile.models import *
from userprofile.mixins import *
from django.views import View
from django.urls import NoReverseMatch, reverse



# Create your views here.
def Index(request):
	return render(request,'index.html')

class Login(OTPMixin,View,AuthUserMixin):
    def post(self,request):
        data = request.POST['phone_no']
        
        try:
            user = Users.objects.get(phone_no=data)
            print(user)
        except Users.DoesNotExist:
        	raise Http404("user does not exist")
            
        if data and user:
            OTP_resp = self.create_otp_record(data)
            print(OTP_resp)
            if not OTP_resp:
                return redirect(request, 'index.html',{'status_code':400,'msg':'OTP exception'})
            resp_json = {
                'status_code':200,
                'user_status':True,
                'message':'OTP sent successfully',
                'user_id': user.id,

                
                        }
            return redirect(request, 'index.html',{"resp_json":resp_json})
        
        else:
            resp_json = {
                'status_code':400,
                'message':'Something went wrong',
                }
            return redirect(request, 'login.html', {'resp_json':resp_json})

class VerifyOTP(OTPMixin,View,AuthUserMixin):
    def post(self, request):
        phone_no = request.POST['phones']
        print(phone_no)
        otp_sent = (request.POST['otp'])
        print(otp_sent)
        userse = Users.objects.get(phone_no=phone_no)
        users = Anonymous.objects.get(phone_no=phone_no)
        print(users)

        obj = OTP.objects.get(user=users)
        if phone_no and otp_sent:
            old = OTP.objects.filter(user=users)
            if old.exists():
                old=old.first()
                otp=old.otp
                if str(otp_sent)==str(otp):

                    old.validate=True
                    old.save()
                    resp = {
                         'message':'OTP successfully Match',
                         'status_code':200,
                         
                            }
                    return render(request, 'userdash.html',{'resp':resp})

                else:
                    
                    return JsonResponse({
                    'message':'OTP is Invalid',
                    'status':False,
                    })
            else:
                return JsonResponse({
                    'status_code':False,
                    'message':'first proceed via sending otp request'
                    })
        else:
                return JsonResponse({
                    'status_code':False,
                    'message':'Please Provide both phone and otp for vailidation'
                    })

        #     auth_resp = self.get_auth_token(userse)
        #     if not auth_resp:
        #         return redirect(request, 'index.html',{'status_code':400,'msg':'OTP exception'})
        #     resp_json = {
		      #   'msg':'OTP successfully verified',
        #         'status_code':200,
        #         'auth_token':auth_resp['auth_token'],
        #         'session_id':auth_resp['session_id']
        #                 }
        #     print(resp_json)
        #     return render(request, 'userdash.html',{'resp':resp_json})
        # else:
        #     resp_json = {
		      #        'msg':'OTP successfully verified',
		      #        'status_code':200,
		      #        'auth_token':'',
		      #        'session_id':''
		      #           }
        #     return render(request, 'userdash.html', {'resp_json':resp_json})                                    
        # # else:
            
        #     return Response({'msg':'Invalid OTP','status_code':400})



        # print(resp)
        # users = Users.objects.get(phone_no=phone_no)
        # obj = OTP.objects.get(user=users)
        # print(obj)
        # if obj.otp==otp:
        # 	# user=Users.objects.get(phone_no=phone_no)
        #  #    auth_resp=self.get_auth_token(user)
        #  #    resp_json={
        #  #                'msg':'OTP successfully verified',
        #  #                'status_code':200,
        #  #                'auth_token':auth_resp['auth_token'],
        #  #                'session_id':auth_resp['session_id']
        #  #                }
            

        #     user.verified = True
        #     #user.otp.delete() 
        #     user.save()
        #     return Response("Verification Successful")
        # else:
        #     raise PermissionDenied("OTP Verification failed")
        

