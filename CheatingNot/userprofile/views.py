from userprofile.models import *
from userprofile.mixins import *
from userprofile.serializers import *
from userprofile.utility import *
from rest_framework.views import APIView
from rest_framework.response import Response 
from subscription.models import UserDailyDose, Wallet
    
            
class RegisterOLogin(AnonymousUSerMixin,OTPMixin,APIView,AuthUserMixin):
    def post(self,request):
        data = request.data.dict()
        try:
            user = Users.objects.get(Q(phone_no=data['phone_no']) or Q(email=data['email']))
        except Users.DoesNotExist:
            user = None
        if data['phone_no'] and user:
            OTP_resp = self.create_otp_record(data)
            if not OTP_resp:
                return Response({'status_code':400,'msg':'OTP exception'})
            resp_json = {
                'status_code':200,
                'user_status':True,
                'msg':'OTP sent successfully',
                'user_id': user.id,
                'auth_token':user.user.auth_token,
                'session_id':''
            }
            return Response(resp_json)
        elif data['email'] and user:
            auth_resp = self.get_auth_token(user)
            resp_json = {
                'user_status':True,
                'msg':'user exists',
                'status_code':200,
                'user_id':user.id,
                'auth_token':auth_resp['auth_token'],
                'session_id':auth_resp['session_id'],
            }
            return Response(resp_json)
        elif data['phone_no']:
            au_resp = self.create_anonymous_user(data)
            if not au_resp['status']:
                return Response(au_resp)
            OTP_resp = self.create_otp_record(data)
            if not OTP_resp:
                return Response({'status_code':400,'msg':'OTP exception'})
            resp_json = {
                'status_code':200,
                'user_status':False,
                'auth_token':au_resp['auth_token'],
                'msg':'OTP sent successfully',
                'user_id': '',
                'session_id':''
            }
            return Response(resp_json)
        elif data['email']:
            au_resp = self.create_anonymous_user(data)
            if not au_resp['status']:
                return Response(au_resp)
            resp_json = {
                'user_status':False,
                'msg':'user not exists',
                'status_code':200,
                'user_id':'',
                'auth_token':au_resp['auth_token'],
                'session_id':'',
            }
            return Response(resp_json)
        else:
            resp_json = {
                'status_code':400,
                'msg':'Something went wrong',
                }
            return Response(resp_json)

        
class ResendOTP(OTPMixin, APIView,AuthUserMixin):
    def put(self, request):
        data = request.data.dict()
        if self.authenticate_anonymous(data['phone_no'], request.META['HTTP_AUTHORIZATION'])['status']:
            if self.create_otp_record(data):
                return Response({'status_code':200,'msg':'OTP sent successfully'})
            else:  
                return Response({'status_code':400,'msg':'Something went wrong'})
        else:
            return Response({'status_code':400, 'msg':"invalid user"})        
        
        
class VerifyOTP(AnonymousUSerMixin,OTPMixin,APIView,AuthUserMixin):
    def post(self, request):
        data = request.data.dict()
        resp  = self.authenticate_anonymous(data['phone_no'], request.META['HTTP_AUTHORIZATION'])
        if resp['status']:
            obj = OTP.objects.get(user=resp['user'])
            if obj.otp == data['otp']:
                if data['user_id']:
                    user = Users.objects.get(id=data['user_id'])
                    auth_resp = self.get_auth_token(user)
                    resp_json = {
                        'msg':'OTP successfully verified',
                        'status_code':200,
                        'auth_token':auth_resp['auth_token'],
                        'session_id':auth_resp['session_id']
                        }
                    return Response(resp_json)
                else:
                    resp_json = {
                        'msg':'OTP successfully verified',
                        'status_code':200,
                        'auth_token':'',
                        'session_id':''
                        }
                    return Response(resp_json) 
            else:
                return Response({'msg':'Invalid OTP','status_code':400})
        else:
            return Response({'msg':'Invalid user','status_code':400})
        

        
class CreateUser(AuthUserMixin, APIView,NotificationMixin):
    def post(self,request):
        data = request.data.dict()
        if data['phone_no']:
            resp  = self.authenticate_anonymous(data['phone_no'], request.META['HTTP_AUTHORIZATION'])
            if not resp['status']:
                return Response({'msg':'Invalid request','status_code':400})
            obj = resp['user']
        elif data['email']:
            resp  = self.authenticate_anonymous(data['phone_no'], request.META['HTTP_AUTHORIZATION'])
            if not resp['status']:
                return Response({'msg':'Invalid request','status_code':400})
            obj = resp['user']
        try:
            dob = datetime.strptime(data['dob'],'%d/%m/%Y').date()
        except:
            return Response({'msg':'Invalid DOB format','status_code':400})
        if data['referral_code']:
            try:
                referrer_amount = Discount.objects.get(id=1).referral_amount
                referrer_user = Users.objects.get(referral_code=data['referral_code'])
                wallet = Wallet.objects.get(user=referrer_user)
                wallet.referral_amount = wallet.referral_amount+referrer_amount
                wallet.wallet_amount = wallet.wallet_amount+referrer_amount
                wallet.save()
                sender = Users.objects.get(email='contact@cheatingnot.com')
                notification_data = {
                    'sender':sender,
                    'receiver':referrer_user,
                    'action':'referral'
                    }
                self.referral_notification(notification_data)
            except Exception as e:
                print('referral code exception --',e)
        data.update({
            'referral_code':data['name'][:4]+str(random.randrange(1000,9999)),
            'user_type'   :'Common',
            'app_version' : obj.app_version,
            'device_id'   : obj.device_id,
            'device_type' : obj.device_type,
            'fcm_token'   : obj.fcm_token,
            'country_code': obj.country_code,
            'dob':dob
            })
        
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = Users.objects.get(Q(phone_no=data['phone_no'],email=data['email']))
            user.active = True
            user.profile_verified = True
            user.profile_complete_percentage = user.profile_complete_percentage + 24
            auth_resp = self.get_auth_token(user)
            user_images = UserprofileImages(user=user, profilepics=data['profile_pic'])
            user_images.is_profile = True
            user_images.save()
            user.save()
            create_user_response = {
                "user_id": user.id,
                'auth_token': auth_resp['auth_token'],
                'session_id': auth_resp['session_id'],
                'msg': 'User created successfully',
                'status_code':200,
                'profile_complete': {
                    'create_user':user.profile_complete_percentage,
                    'add_photos':0,
                    'add_videos':0,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                    }
                }
            return Response(create_user_response)
        if serializer.errors:
            print(serializer.errors)
            return Response({'msg':'something went wrong','error':serializer.errors})

            
    def put(self,request):
        data = request.data.dict() 
        
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        user = resp['user']
        if user.profile_update_percentage >  0:
            pass
        else:
            user.profile_update_percentage = 20
            user.profile_complete_percentage = user.profile_complete_percentage + 20
        height = Height.objects.get(id=data['height']).height
        weight = Weight.objects.get(id=data['weight']).weight
        occupation = Occupation.objects.get(id=data['occupation']).occupation
        data.update({'height':height,'weight':weight,'occupation':occupation})
        serializer = UserUpdateSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            user.save()
            return Response({
                'msg':'resource updated successfully',
                'status_code':200,
                'profile_complete': {
                    'create_user':24,
                    'add_photos':(user.profilepics.count()-1) * 3,
                    'add_videos': user.profilevideos.count() * 3,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                    }
                })
        if serializer.errors:
            print(serializer.errors)
            print('user update errors--',serializer.errors)
            return Response({'msg':'something went wrong','status_code':400})
        

class SuspendUser(AuthUserMixin,APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user = resp['user']
        user.is_active = False
        user.save()
        return Response({
            'msg':'User Deactivated Successfully',
            'status_code':200
            })

   
            
class AddPhoto(AuthUserMixin,APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        try:
            user = resp['user']
            if user.profilepics.count() > 7:
                return Response({'msg':'you cannot add more then 6 images','status_code':400})
            user_images = UserprofileImages(user=user, profilepics=data['profile_pic'])
            if data['is_profile'] == 'True':
                user.profilepics.filter(is_profile=True).update(is_profile=False)
                user_images.is_profile = data['is_profile']
                user_images.save()
            else:
                user_images.is_profile = data['is_profile']
                user_images.save()
            user.profile_complete_percentage = user.profile_complete_percentage + 3 
            user.save()
                
            return Response({  
                'msg':'Image uploaded successfully',
                'status_code':200,
                'profile_complete': {
                    'create_user':24,
                    'add_photos':(user.profilepics.count()-1) *3,
                    'add_videos':user.profilevideos.count() *3,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                }
            })
        except Exception as e:
            print(e)
            return Response({'msg':'Image Not Found','status_code':400})
        
    
    
class DeletePhoto(AuthUserMixin,APIView):
    def post(self,request):
        data  = request.data.dict()
        print('delete photo data',data)
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)  
        image_id = 'profiles/'+data['image_id']
        try:
            user = resp['user']
            UserprofileImages.objects.get(profilepics=image_id).delete()
            user.profile_complete_percentage = user.profile_complete_percentage - 3
            user.save()
            return Response({
                'msg':'Image uploaded successfully',
                'status_code':200,
                'profile_complete': {
                    'create_user':24,
                    'add_photos':(user.profilepics.count()-1) *3,
                    'add_videos':user.profilevideos.count() *3,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                }
            })
        except UserprofileImages.DoesNotExist:
            return Response({'msg':'Image Not Found','status_code':400})
        
            
def get_video_url(user):
    serializer = VedioThumbnailSerializer(user)
    print(serializer.data)
    for v in len(serializer.data['profilevideos']-1,-1,-1):
        v_data = dict(v)
    return v_data

        
class AddVideo(AuthUserMixin,APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        try:
            user = resp['user']
            if user.profilevideos.count() > 6:
                return Response({'msg':'you cannot add more then 6 videos','status_code':400})  
            vedio = UserprofileVideos(user=user, profilevideos=data['profile_video'])
            vedio.profilevideos.name = str(vedio.profilevideos.name)
            vedio.save()
            url = UserprofileVideos.objects.filter(user=user).last().serializable_value('profilevideos').url
            user.profile_complete_percentage = user.profile_complete_percentage + 3
            user.save()
            return Response({
                'msg':'Image uploaded successfully',
                'status_code':200,
                'url':url,
                'profile_complete': {
                    'create_user':24,
                    'add_photos':(user.profilepics.count()-1) *3,
                    'add_videos':user.profilevideos.count() *3,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                }
            })
        except Exception as e:
            print(e)
            return Response({'msg':'something went wrong','status_code':400,'error':str(e)})    
        
    
class DeleteVedio(AuthUserMixin,APIView):
    def post(self,request):
        data  = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        video_id = 'profiles_vedios/'+data['video_id']
        try:
            user = resp['user']
            UserprofileVideos.objects.get(profilevideos=video_id).delete()
            user.profile_complete_percentage = user.profile_complete_percentage - 3
            user.save()
            return Response({
                'msg':'Image uploaded successfully',
                'status_code':200,
                'profile_complete': {
                    'create_user':24,
                    'add_photos':(user.profilepics.count()-1) *3,
                    'add_videos':user.profilevideos.count() *3,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                }
            })
        except UserprofileVideos.DoesNotExist:
            return Response({
                'msg':'Video not found',
                'status_code':400
                })
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def index(request):
    return  Response({
        'msg':"Welcome to Home page"
    })
        
class UserPreferences(AuthUserMixin,APIView):
    def put(self,request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        user = resp['user']        
        preferences = Preferences.objects.get(user=user)
        serializer = PrefranceUpdateSerializer(preferences, data=data)
        if serializer.is_valid():
            serializer.save()
            if user.preferences.preferences_update_percentage > 0:
                pass
            else:
                user.preferences.preferences_update_percentage = 20
                user.profile_complete_percentage = user.profile_complete_percentage + 20
                user.save()
            return Response({
                'msg':'preferences updated successfully',
                'status_code':200,
                'profile_complete': {
                    'create_user':24,
                    'add_photos':(user.profilepics.count()-1) *3,
                    'add_videos':user.profilevideos.count() *3,
                    'profile_update':user.profile_update_percentage,
                    'preferences':user.preferences.preferences_update_percentage,
                    'total_percentage':user.profile_complete_percentage
                }
            })
        if serializer.errors:
            return Response({
                'msg':'updated not',
                'error':serializer.errors,
                'status_code':400
                })
    
         
class UserInfo(AuthUserMixin,APIView):
    def get(self,request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user = resp['user']
        if user.active:
            serializer = UserInfoSerializer(user)
            user_data = serializer.data
            user_data.update({
                'profile_complete': {
                        'create_user':24,
                        'add_photos':(user.profilepics.count()-1) *3,
                        'add_videos':user.profilevideos.count() *3,
                        'profile_update':user.profile_update_percentage,
                        'preferences':user.preferences.preferences_update_percentage,
                        'total_percentage':user.profile_complete_percentage
                    }
                })
            user_data.update({
                'notifications_count':{
                    'likes': Like.objects.filter(liked=user).count(),
                    'suprelikes': SuperLike.objects.filter(superliked=user).count(),
                    'hearts': Heart.objects.filter(heart_to=user).count(),
                    'matches': Match.objects.filter(matches=user).count()
                    }
                })
            return Response(user_data) 
        else:
            return Response({
                'msg':'User profile picture is vulgar',
                'status_code':200,
                "data":'no data'
                })
            
            
class NotificationsUsersDetails(AuthUserMixin,APIView):
    def get(self,request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        user = resp['']
        if data['likes']:
            page_start = data['page_start']
            page_end = data['page_end']
            users = Users.objects.filter(Like.objects.filter(liked=user).order_by('-create_at')[page_start:page_end].values_list('liked_id',flat=True))
        elif data['superlikes']:
            page_start = data['page_start']
            page_end = data['page_end']
            users = Users.objects.filter(SuperLike.objects.filter(superliked=user).order_by('-create_at')[page_start:page_end].values_list('superliked_id',flat=True))
        elif data['hearts']:
            page_start = data['page_start']
            page_end = data['page_end']
            users = Users.objects.filter(Heart.objects.filter(liked=user).order_by('-create_at')[page_start:page_end].values_list('heart_to_id',flat=True))
        elif data['matches']:
            page_start = data['page_start']
            page_end = data['page_end']
            users = Users.objects.filter(Match.objects.filter(matches=user).order_by('-create_at')[page_start:page_end].values_list('matches_id',flat=True))
        else:
            return Response({'msg':'something went wrong','status_code':400})
        
        serializer = UserlistingSerializer(users, many=True,context={'user_id': data['user_id']})
        return Response({'data':serializer.data})
        
                
class DropDownList(APIView):
    def get(self, request):
        hobbies_serializer    = HobbiesSerializer(Hobbies.objects.all(), many=True)
        height_serializer     = HeightSerializer(Height.objects.all(), many=True)
        weight_serializer     = WeightSerializer(Weight.objects.all(), many=True)
        occupation_serializer = OccupationSerializer(Occupation.objects.all(), many=True)
        
        return Response({
            'status': True, 
             'message': 'success',
             'height': height_serializer.data,
             'weight': weight_serializer.data,
             'occupation': occupation_serializer.data,
             'hobbies':hobbies_serializer.data
        })
        

def is_user_blocked(pk):
    blocked_by = list(set(Block.objects.filter(blocked_user=pk).values_list('blocked_by',flat=True)))
    if blocked_by:
        return blocked_by
    else:
        return False
    
class UserNopes(AuthUserMixin, APIView, NotificationMixin):   
    def post(self,request):  
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user  = resp['user']
        try:
            nope_user = Users.objects.get(id=data['nope_id'])
        except Users.DoesNotExist:
            return Response({'msg':"Nope user not find",'status_code':400})
        nope = Nopes(user=user,nope=nope_user)
        nope.save()
        return Response({'msg':'nope user added successfully'})
     
class UserLikes(AuthUserMixin, APIView, NotificationMixin):   
    def post(self,request):  
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user  = resp['user']
        userdose  = UserDailyDose.objects.get(user=user) 
        try:
            liked_user = Users.objects.get(id=data['liked_id'])
        except Users.DoesNotExist:
            return Response({"msg":'liked user not found','status_code':400})
        if userdose.remaining_likes > 0:
            if Hi.objects.filter(hi_to=user).exists() or Like.objects.filter(liked=user).exists() or \
                Heart.objects.filter(heart_to=user).exists() or SuperLike.objects.filter(superliked=user).exists():
                match = Match.objects.create(user=user)
                match.matches.add(liked_user)
                match.save()
                notification_data = {
                    "sender": user,
                    'receiver':liked_user,
                    'action': 'match' 
                }
                self.user_notification(notification_data)
                userdose.remaining_likes  = userdose.remaining_likes - 1
                userdose.save()
                return Response({
                    'msg':"it's match",
                    'status_code':200,
                    'remaining_likes':userdose.remaining_likes
                    })
            else:
                like = Like.objects.create(user=user,liked=liked_user)
                like.save()
                userdose.remaining_likes  = userdose.remaining_likes - 1
                userdose.save()
                self.user_notification(notification_data)
                return Response({
                    'msg':'like successful',
                    'status_code':200,
                    'remaining_like':userdose.remaining_likes
                    })
        else:
            return Response({
                'msg':'Your daily limit is over',
                'status_code':201,
                'remaining_likes':userdose.remaining_likes
                })

class UserSuperLikes(AuthUserMixin, APIView, NotificationMixin):     
    def post(self,request):  
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user  = resp['user']
        userdose  = UserDailyDose.objects.get(user=user) 
        try:
            superliked_user = Users.objects.get(id=data['superliked_id'])
        except Users.DoesNotExist:
            return Response({"msg":'super liked user not found','status_code':400})
        if userdose.remaining_superlikes > 0:
            if (Hi.objects.filter(hi_to=user).exists() or 
                Like.objects.filter(liked=user).exists() or 
                Heart.objects.filter(heart_to=user).exists() or 
                SuperLike.objects.filter(superliked=user).exists()):
                
                match = Match.objects.create(user=user)
                match.matches.add(superliked_user)
                match.save()
                notification_data = {
                    "sender": user,
                    'receiver':superliked_user,
                    'action': 'match' 
                }
                self.user_notification(notification_data)
                userdose.remaining_superlikes = userdose.remaining_superlikes-1
                userdose.save()
                return Response({
                    'msg':"it's match",
                    'status_code':200,
                    'remaining_superlikes':userdose.remaining_superlikes
                    })
            else:
                superlike, _ = SuperLike.objects.get_or_create(user=user,superliked=superliked_user)
                superlike.superlike_count = superlike.superlike_count + 1 
                superlike.save()
                userdose.remaining_superlikes = userdose.remaining_superlikes-1
                userdose.save()
                notification_data = {
                    "sender": user,
                    'receiver':superliked_user,
                    'action': 'superlike' 
                }
                self.user_notification(notification_data)
                return Response({
                    'msg':'superlike sends successfuly',
                    'status_code':200,
                    'remaining_superlikes':userdose.remaining_superlikes
                    })
        else:
            return Response({
                'msg':'Your superlike is over',
                'status_code':201,
                'remaining_superlikes':userdose.remaining_superlikes
                })



class UserHearts(AuthUserMixin, APIView, NotificationMixin):     
    def post(self,request):  
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user  = resp['user']
        userdose  = UserDailyDose.objects.get(user=user) 
        try:
            heart_user = Users.objects.get(id=data['heart_id'])
        except Users.DoesNotExist:
            return Response({"msg":'Heart sends user not found','status_code':400})
        if userdose.remaining_hearts > 0:
            if (Hi.objects.filter(hi_to=user).exists() or 
                Like.objects.filter(liked=user).exists() or 
                Heart.objects.filter(heart_to=user).exists() or
                SuperLike.objects.filter(superliked=user).exists()):
                match = Match.objects.create(user=user)
                match.matches.add(heart_user)
                match.save()
                
                notification_data = {
                    "sender": user,
                    'receiver':heart_user,
                    'action': 'match' 
                }
                self.user_notification(notification_data)
                return Response({
                    'msg':"it's match",
                    'status_code':200,
                    'remaining_hearts':userdose.remaining_hearts
                    })
            else:
                heart, _= Heart.objects.get_or_create(user=user,heart_to=heart_user)
                heart.heart_count = heart.heart_count + 1 
                heart.save()
                userdose.remaining_hearts = userdose.remaining_hearts - 1 
                userdose.save()
                
                notification_data = {
                    "sender": user,
                    'receiver':heart_user,
                    'action': 'heart' 
                }
                self.user_notification(notification_data)
                return Response({
                    'msg':'heart sends successfully',
                    'status_code':200,
                    'remaining_hearts':userdose.remaining_hearts
                    })
        else:
            return Response({
                'msg':'Your Heart is over',
                'status_code':201,
                'remaining_hearts':userdose.remaining_hearts
                })




class UserHi(AuthUserMixin, APIView, NotificationMixin):     
    def post(self,request):  
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        user  = resp['user']
        userdose  = UserDailyDose.objects.get(user=user) 
        try:
            hi_user = Users.objects.get(id=data['hi_id'])
        except Users.DoesNotExist:
            return Response({"msg":'Heart sends user not found','status_code':400})
        if userdose.remaining_hi > 0:
            if (Hi.objects.filter(hi_to=user).exists()
                or Like.objects.filter(liked=user).exists() 
                or Heart.objects.filter(heart_to=user).exists() 
                or SuperLike.objects.filter(superliked=user).exists()):
                match = Match.objects.create(user=user)
                match.matches.add(hi_user)
                match.save()
                notification_data = {
                    "sender": user,
                    'receiver':hi_user,
                    'action': 'match' 
                }
                self.user_notification(notification_data)
                userdose.remaining_hi = userdose.remaining_hi - 1
                userdose.save()
                return Response({
                    'msg':"it's match",
                    'status_code':200,
                    'remaining_hi':userdose.remaining_hi
                    })
            else:
                
                hi, _ = Hi.objects.get_or_create(user=user,hi_to=hi_user)
                hi.hi_count = hi.hi_count+1
                hi.save()
                userdose.remaining_hi = userdose.remaining_hi - 1
                userdose.save()
                notification_data = {
                    "sender": user,
                    'receiver':hi_user,
                    'action': 'hi' 
                }
                self.user_notification(notification_data)
                return Response({
                    'msg':'heart sends successfully',
                    'status_code':200,
                    'remaining_hi':userdose.remaining_hi
                    })
        else:
            return Response({
                'msg':'Your Heart is over',
                'status_code':201,
                'remaining_hi':userdose.remaining_hi
                })


class MyLikes(AuthUserMixin, APIView, NotificationMixin):
    def get(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        user  = resp['user']
        if int(data['page']) == 1:
            row_from = 0
            row_to = 10
        else:
            row_from = (int(data['page'])-1) *2
            row_to = int(data['page']) *2
        likes = Like.objects.filter(user=user).order_by('-create_at')#[row_from:row_to]
        likes_ids = likes.values_list('liked_id',flat=True)
        users = Users.objects.filter(id__in=likes_ids)
        serializer = UserlistingSerializer(users, many=True,context={'user_id': data['user_id']})
        return Response(serializer.data)


class MyMatches(AuthUserMixin, APIView, NotificationMixin):
    def get(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        user  = resp['user']
        start_page = data['start_page']
        end_page = data['end_page']
        matches = Match.objects.filter(user=user).order_by('-create_at').values_list('matches_id',flat=True)[start_page:end_page]
        users = Users.objects.filter(user_id=matches)
        serializer = UserlistingSerializer(users, many=True)
        return Response(serializer.data)



class UserListing(AuthUserMixin, APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            return Response(resp)
        
        user = resp['user']
        user.latitude = data['latitude']
        user.longitude = data['longitude']
        user.save()
        gender = Preferences.objects.get(user=user).gender
        
        params = Users.objects.filter().order_by('?')[:10]
        serializer = UserlistingSerializer(params, many=True,context={'user_id': data['user_id']})
        return Response({'data':serializer.data})
        
        if data['all']:
            if gender in ['male','female']:
                params = Users.objects.filter(admin=False,gender=gender).order_by('?')[:10]
            else:
                params = Users.objects.filter(admin=False).order_by('?')[:10]
            serializer = UserlistingSerializer(params, many=True,context={'user_id': data['user_id']})
            respdata = to_dict(serializer.data)
            origin = {'latitude':float(data['latitude']),'longitude':float(data['longitude'])}
            sorted_data = self.short_locations(origin, respdata)
            return Response({'data':sorted_data})
        elif data['nearby']:
            if gender in ['male','female']:
                params = Users.objects.filter(admin=False,gender=gender).order_by('?')[:10]
            else:
                params = Users.objects.filter(admin=False).order_by('?')[:10]
        elif data['online']:
            if gender in ['male','female']:
                params = Users.objects.filter(admin=False,gender=gender).order_by('?')[:10]
            else:
                params = Users.objects.filter(admin=False).order_by('?')[:10]
            serializer = UserlistingSerializer(params, many=True,context={'user_id': data['user_id']})
            respdata = to_dict(serializer.data)
            origin = {'latitude':float(data['latitude']),'longitude':float(data['longitude'])}
            sorted_data = self.short_locations(origin, respdata)
            return Response({'data':sorted_data})
        elif data['new']:
            if gender in ['male','female']:
                params = Users.objects.filter(admin=False,gender=gender,create_at=datetime.date()).order_by('?')[:10]
            else:
                params = Users.objects.filter(admin=False,create_at=datetime.date()).order_by('?')[:10]
            serializer = UserlistingSerializer(params, many=True,context={'user_id': data['user_id']})
            respdata = to_dict(serializer.data)
            origin = {'latitude':float(data['latitude']),'longitude':float(data['longitude'])}
            sorted_data = self.short_locations(origin, respdata)
            return Response({'data':sorted_data})
        elif data['vedio']:
            if gender in ['male','female']:
                params = Users.objects.filter(admin=False,gender=gender).order_by('?')[:10]
            else:
                params = Users.objects.filter(admin=False).order_by('?')[:10]
            serializer = VediosSerializers(params, many=True,context={'user_id': data['user_id']})
            respdata = to_dict(serializer.data)
            origin = {'latitude':float(data['latitude']),'longitude':float(data['longitude'])}
            sorted_data = self.short_locations(origin, respdata)
            return Response({'data':sorted_data})
        else:
            if gender in ['male','female']:
                params = Users.objects.filter(admin=False,gender=gender).order_by('?')[:10]
            else:
                params = Users.objects.filter(admin=False).order_by('?')[:10]
            serializer = UserlistingSerializer(params, many=True,context={'user_id': data['user_id']})
            respdata = to_dict(serializer.data)
            origin = {'latitude':float(data['latitude']),'longitude':float(data['longitude'])}
            sorted_data = self.short_locations(origin, respdata)
            return Response({'data':sorted_data})
        
        
class UserSearch(AuthUserMixin, APIView):
    def post(self, request):
        data = request.data.dict()
        resp = self.authenticate_user(data['user_id'], request.META['HTTP_AUTHORIZATION'])
        if not resp['status']:
            resp.update({'status_code':400})
            return Response(resp)
        
        user = resp['user']
        gender = Preferences.objects.get(user=user).gender
        search_text = data['search_text'].title()
        data = request.data.dict()
        if gender == 'both':
            params = Users.objects.filter(admin=False,fullname__startswith=search_text)\
            .exclude(id__in=list(Like.objects.values_list('liked_to_id',flat=True).filter(user=user)))\
            .exclude(id=user.id)\
            .exclude(id__in=list(Heart.objects.filter(heart_to=user.user_id).values_list('user_id',flat=True)))\
            .exclude(id__in=list(set(Block.objects.filter(blocked_by=user.user_id).values_list('blocked_user',flat=True))))\
            .exclude(id__in=list(Match.matches.through.objects.filter(match_id=user.user_id).values_list('user_id',flat=True)))
        else:
            params = Users.objects.filter(admin=False,fullname__startswith=search_text)\
            .exclude(id__in=list(Like.objects.values_list('liked_to_id',flat=True).filter(user=user)))\
            .exclude(id=user.id)\
            .exclude(id__in=list(Heart.objects.filter(heart_to=user.user_id).values_list('user_id',flat=True)))\
            .exclude(id__in=list(set(Block.objects.filter(blocked_by=user.user_id).values_list('blocked_user',flat=True))))\
            .exclude(id__in=list(Match.matches.through.objects.filter(match_id=user.user_id).values_list('user_id',flat=True)))
            
        serializer = UserlistingSerializer(params, many=True,context={'user_id': user.user_id})
        try:
            respdata = to_dict(serializer.data)
        except Exception as e:
            print(e)
        return Response({'status': True, 'message': 'Done', 'data': respdata})
    
class Notification(APIView):
    def get(self, request, user_id):
        try:
            data = UsersNotification.objects.filter(currentuser_id=user_id).order_by('-create_at')
            try:
                user = Users.objects.get(pk=user_id)
                user.last_login = datetime.now()
                user.active = True
                user.save()
            except Exception as e:
                print('Users notification exceptions',e)
                return Response({'status': False, 'message': str(e)})
        except:
            return Response({'status': False, 'message': 'User not found'})
        if data:
            serializer = UsersNotificationSerializer(data, many=True, context={'userid': 'id'})
            return Response({'status': True, 'message': 'successfully', 'notification': serializer.data})
        return Response({'status': False, 'message': 'No Data'})
 
    def post(self, request, pk):
        if request.data['delete'] == 'clearall':
            UsersNotification.objects.filter(currentuser=pk).delete()
            return Response({'status': False, 'message': 'successfully cleared'})
        elif request.data['delete'] == 'clear' and request.data['notificationid']:
            try:
                UsersNotification.objects.get(pk=request.data['notificationid']).delete()
                return Response({'status': True, 'message': 'Successfully'})
            except:
                return Response({'status': False, 'message': 'Unsuccessfully'})
        return Response({'status': False, 'message': 'something wrong with you'})
    
    
    
# class MyLikes(AuthUserMixin, APIView):
#     def get(self,request,user_id):
#         resp = self.authenticate_user(user_id, request.META['HTTP_AUTHORIZATION'])
#         if not resp['status']:
#             resp.update({'status_code':400})
#             return Response(resp)
#         user = resp['user']
#         likes = list(Like.objects.filter(user=user).values_list('liked_to',flat=True))
#         liked_users = Users.objects.filter(id__in=likes)
# #         serializer = GetLikedByMeSerializer(liked_users, many=True)
# #         print('****************',serializer.data)
#         return Response({'data':'data'})
        
        
                 
