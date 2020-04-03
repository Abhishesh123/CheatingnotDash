import requests
import json
import random
import math






URL = 'https://www.sms4india.com/api/v1/sendCampaign'

# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
    
    req_params = {
    'apikey':apiKey,
    'secret':secretKey,
    'usetype':useType,
    'phone': phoneNo,
    'message':textMessage,
    'senderid':senderId
    }
    return requests.post(reqUrl, req_params)


digits = "0123456789"
otp = ''
for i in range(4):    
    otp += digits[math.floor(random.random() * 10)] 


msg = f"Please dear your one time password is {otp}"




# get response
response = sendPostRequest(URL, 'api-key', 'secretKey', 'stage', phone, 'SMSIND', msg )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print(response.text)
