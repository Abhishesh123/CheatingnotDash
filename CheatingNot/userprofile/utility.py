import json
import random
import re
import requests

   
def is_valid_json(data):
    try:
        p_data = json.loads(data)
#         print(p_data)
        json_data = {'status':True,'msg':'Please provide a valid data','data':p_data}
        return json_data
    except:
        json_data = {'status':False,'msg':'Please provide a valid data'}
        return (json_data)

def send_otp(data):
    msg91key, appHashKey = ('263002Ai7e8CMeu55c6662f1','vZzy1MwDoHp') # msg91 auth keys
    req = 'http://control.msg91.com/api/sendotp.php?authkey={0}&message=%3C%23%3E%20{1}\
    OTP for CheatingNot mobile verification {2} &sender=CHTNOT&mobile={3}{4}\
    &otp={5}'.format(msg91key,data['otp'],appHashKey,data['country_code'],data['phone_no'],data['otp'])
    resp = requests.get(re.sub(' +',' ',req), headers={"content-type": "application/json"})#sending request to send OTP
    print('OTP sent successfully')
    print(resp.status_code,'---',resp.json())


def get_referral():
    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ch = random.choice(l) + random.choice(l)
    num = random.randrange(100000,999999)
    
from json import dumps,loads
def to_dict(input_ordered_dict):
    return loads(dumps(input_ordered_dict))


