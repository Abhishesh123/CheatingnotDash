import uuid
from userprofile.models import *
from datetime import datetime, timedelta
import random
from CheatingNot.settings import FCMKEY


class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json', status=status)


def check_otp_duration(otp_created_time):
    otp_created_time = otp_created_time.timestamp()
    time_diff = datetime.now().timestamp() - otp_created_time
    return int(time_diff)

class AuthUserMixin(object):
    def authenticate_user(self,user_id,auth_token):
        try:
            user = Users.objects.get(id=user_id)
            if user.userauth.auth_token == auth_token:
                return {'status':True,'user':user, 'msg':'user exists'}
            else:
                return {'status':False, 'msg':'Invalid Authorization token','status_code':400}
        except  Exception as e:
            print(str(e))
            return {'status':False,'msg':"Invalid user",'status_code':400}
        
    def authenticate_anonymous(self,phone_no,auth_token):
    
        if Anonymous.objects.filter(phone_no=phone_no,auth_token=auth_token).exists():
            return {'status':True, 'user': Anonymous.objects.get(phone_no=phone_no)}
        else:
            return {'status':False, 'user': None}
                    
    def get_auth_token(self,user):
        auth_token = str(uuid.uuid4().hex)
        session_id = str(uuid.uuid4().hex)
        user, _ = UserAuth.objects.get_or_create(user=user)
        user.auth_token = auth_token
        user.session_id = session_id
        user.save()
        return {'auth_token':auth_token, 'session_id':session_id}
    
    
    
    def get_user_id(self):
        return str(uuid.uuid4().hex)[:20]
        

class AnonymousUSerMixin(object):
    def create_anonymous_user(self,data):
        if data['phone_no']:
            try:
                token = str(uuid.uuid4().hex)
                au, _ = Anonymous.objects.get_or_create(phone_no=data['phone_no'],app_version=data['app_version'])
                au.country_code = data['country_code']
                au.email = ''
                au.auth_token = token
                au.device_id = data['device_id']
                au.device_type = data['device_type']
                au.device_id = data['device_id']
                au.fcm_token = data['fcm_token']
                au.save()
                return {'auth_token':token,'status':True}
            except Exception as e:
                print('anonymous user not created --{} exception is--{}'.format(data['phone_no']),str(e))
                return {'error':str(e),'status':False,'status_code':400}
        else:
            try:
                token = str(uuid.uuid4().hex)
                au, _ = Anonymous.objects.get_or_create(email=data['email'],app_version=data['app_version'])
                au.phone_no = ''
                au.device_id = data['device_id']
                au.auth_token = token
                au.device_type = data['device_type']
                au.device_id = data['device_id']
                au.fcm_token = data['fcm_token']
                au.save()
                return {'auth_token':token,'status':True}
            except Exception as e:
                print('anonymous user not created --{} exception is--{}'.format(data['email']),str(e))
                return {'error':str(e),'status':False,'status_code':400}
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
            user = Anonymous.objects.get(phone_no=data['phone_no'])
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
        
    
    
from pyfcm import FCMNotification    

notification_choices = ((1, 'like'), (2, 'superlke'), (3, 'heart'),(4,'match'))
notification_type = {'hi':1,'like':2,'superlike':3,'heart':4,'match':5,'referral':6}

class NotificationMixin(object): 
    def send_notification(self,fcm_token,data):
        push_service = FCMNotification(FCMKEY)
        result = push_service.notify_single_device(registration_id=fcm_token, data_message=data)
        print(result)
    
    def admin_notification(self,data):
        sender     = data['sender']
        receiver = data['receiver']
        msg = PushNotificationMsg.objects.get(notification_type=notification_type[data['referral']])
        title = '{}'.format(msg.msg_title)
        msgbody = '{} <b> {} </b>'.format(sender.name, msg)
        url = UserprofileImages.objects.filter(user=sender).last().serializable_value('profilepics').url
        data = {'userid' :sender.id,'msgbody':msgbody,'msgtitle':title,
                'image_url':url,'name':'CheatingNot','phone':sender.phone_no
                }
        self.send_notification(receiver.fcm_token,data)
        

        
        
    def referral_notification(self,data):
        print(data)
        sender     = data['sender']
        receiver = data['receiver']
        msg = PushNotificationMsg.objects.get(notification_type=notification_type[data['action']])
        title = '{}'.format(msg.msg_title)
        msgbody = '{} <b> {} </b>'.format(receiver.name, msg)
        url = UserprofileImages.objects.filter(user=sender).last().serializable_value('profilepics').url
        notificaton_data = {'userid' :str(sender.id),'msgbody':msgbody,'msgtitle':title,
                'image_url':url,'name':'CheatingNot','phone':sender.phone_no
                }
        u = UsersNotification(user=sender,friend_user=receiver)
        u.msg_title = title
        u.msg_body = msgbody
        u.action = data['action'] 
        u.save()
        self.send_notification(receiver.fcm_token,notificaton_data)
        
        
        
    
    def user_notification(self,data):
        push_service = FCMNotification(FCMKEY)
        sender     = data['sender']
        receiver = data['receiver']
        if data['action'] in ['like','heart','superlike','hi']:
            url = UserprofileImages.objects.filter(user=sender).last().serializable_value('profilepics').url
            msg = PushNotificationMsg.objects.get(notification_type=notification_type[data['action']])
            title = '{}'.format(msg.msg_title)
            msgbody = '{} <b> {} </b>'.format(sender.name, msg)
            notificaton_data = {
                'userid' : str(sender.id),
                'msgbody':msgbody,
                'msgtitle':title,
                'image_url':url,
                'name':sender.name,
                'phone':sender.phone_no
                }
            u = UsersNotification(user=sender,friend_user=data['receiver'])
            u.frnduser_id = receiver.id
            u.msgtitle = title
            u.msgbody = msgbody
            u.action = notificaton_data['action'] = data['action']
            u.save()
            self.send_notification(receiver.fcm_token,notificaton_data)
            return
#             result = push_service.notify_single_device(registration_id=receiver.fcm_token, data_message=jsondata)
            
        elif data['action'] == 'match':
            url = UserprofileImages.objects.filter(user=receiver).last().serializable_value('profilepics').url
            msg = PushNotificationMsg.objects.get(notification_type=notification_type[data['action']])
            title = '{}'.format(msg.msg_title)
            msgbody = '{} <b> {} </b>'.format(receiver.name, msg)
            
            resp_data_for_user1 = {
                'userid' :receiver.id,
                'msgbody':msgbody,
                'msgtitle':title,
                'image_url':url,
                'name':receiver.name,
                'phone':receiver.phone_no
                }
            u = UsersNotification(currentuser_id=data['frnduser'])
            u.frnduser_id = data['currentuser']
            u.msgtitle = title
            u.msgbody = msgbody
            u.action = jsondata['action'] = data['action']
            u.save()
            """ sending match notification to user liked by user """
            result = push_service.notify_single_device(registration_id=sender.fcm_token, data_message=resp_data_for_user1)
            
            
            """ sending match notification to liked your"""
            url = UserprofileImages.objects.filter(user=sender).last().serializable_value('profilepics').url
            msg = PushNotificationMsg.objects.get(notification_type=notification_type[data['action']])
            title = '{}'.format(msg.msg_title)
            msgbody = '{} <b> {} </b>'.format(sender.name, msg)
            resp_data_for_user2 = {
                'userid' :sender.id,
                'msgbody':msgbody,
                'msgtitle':title,
                'image_url':url,
                'name':sender.name,
                'phone':sender.phone_no
                }
            u = UsersNotification(currentuser_id=data['frnduser'])
            u.frnduser_id = data['currentuser']
            u.msgtitle = title
            u.msgbody = msgbody
            u.action = jsondata['action'] = data['action']
            u.save()
            result = push_service.notify_single_device(registration_id=receiver.fcm_token, data_message=resp_data_for_user2)
        print(result)
        
        
from math import sin, cos, sqrt, atan2, radians, ceil

class DistanceMatrix(object):
    
    def distance_short_matrix(self,origin,distances):
        """
        Def : This function used to short distances(latitude,longitude) from a origin point(latitude and longitude)
        Params : origin point as a latitude and longitude and all distances list\n
        Return :sorted distances list.
        """
        lat1 = radians(float(origin['lat']))
        lon1 = radians(float(origin['long']))
        R = 6373.0
        locations = []
        if lat1 in [0.0,'0.0'] or lon1 in [0.0,'0.0']:
            for distance in distances:
                distance.update({'distance':'','likes':Like.objects.filter(liked_id=distance['id']).count()})
                locations.append(distance)
        else:
            locations = []
            for distance in distances:
                lat2 = radians(float(distance['latitude']))
                lon2 = radians(float(distance['longitude']))
                dlon = lon2 - lon1
                dlat = lat2 - lat1
    
                a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #             like_count = Likes.objects.filter(liked_id=distance['id']).count()#.values_list('liked_by_id',flat=True)
                if lat2 in [0.0,'0.0']:
                    distance.update({'distance':0,'likes':Like.objects.filter(liked_id=distance['id']).count()})
                else:
                    distance.update({'distance':ceil(R * c),'likes':Like.objects.filter(liked_id=distance['id']).count()})
                locations.append(distance)
        return locations
    
    
    
    def short_locations(self,origin,locations):
       
        origin = {'latitude':float(origin['latitude']),'longitude':float(origin['longitude'])}
        locations_list = self.distance_short_matrix(origin,locations)
        sorted_x = sorted(locations_list, key = lambda i: i['distance'])
        return sorted_x

