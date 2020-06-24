import uuid
from userprofile.models import *
from datetime import datetime, timedelta
import random
from CheatingNot.settings import FCMKEY
import requests
import re          
class OTPMixin(object):
    
    def send_OTP(self,phone_no, OTP, country_code):
        msg91key, appHashKey = ('263002Ai7e8CMeu55c6662f1','vZzy1MwDoHp') # msg91 auth keys
        req = 'http://control.msg91.com/api/sendotp.php?authkey={0}&message=%3C%23%3E%20{1}\
            OTP for CheatingNot mobile verification {2} &sender=CHTNOT&mobile={3}{4}\
            &otp={5}'.format(msg91key,OTP, appHashKey, country_code, phone_no, OTP)
        resp = requests.get(re.sub(' +',' ',req), headers={"content-type": "application/json"})#sending request to send OTP
        print('OTP sent successfully')
        print(resp.status_code,'---',resp.json())
        
    def create_otp_record(self,data):
        try:
            user = Anonymous.objects.get(phone_no=data)
        except:
            user = None
        if user:
            obj, _ = OTP.objects.get_or_create(user=user)
            if obj.otp and obj.otp_expire_at.timestamp() > datetime.now().timestamp():
                self.send_OTP(user.phone_no, obj.otp, user.country_code)
            else:
                obj.otp  = random.randrange(1000, 9999)
                obj.otp_expire_at = datetime.now() + timedelta(hours=1)
                obj.save()
                self.send_OTP(user.phone_no, obj.otp, user.country_code)
            return True
        else:
            return False
        
    
    