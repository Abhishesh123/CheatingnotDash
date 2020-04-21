from rest_framework import serializers
from userprofile.models import *
from django.db.models import Q
from datetime import datetime



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = '__all__'

#         
    def create(self,validated_data):
        return Users.objects.create(**validated_data)
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('name','gender','body_type','about_me','user_type',
                  'height','weight','latitude','longitude','priority',
                  'active','app_version','device_id','device_type',
                  'fcm_token'
                  )
    def update(self, instance, validated_data):
        instance.name       = validated_data.get('name', instance.name)
        instance.gender     = validated_data.get('gender', instance.gender)
        instance.body_type  = validated_data.get('body_type', instance.body_type)
        instance.about_me   = validated_data.get('about_me', instance.about_me)
        instance.user_type  = validated_data.get('user_type', instance.user_type)
        instance.height     = validated_data.get('height', instance.height)
        instance.weight     = validated_data.get('weight', instance.weight)
        instance.latitude   = validated_data.get('latitude', instance.latitude)
        instance.longitude  = validated_data.get('longitude', instance.longitude)
        
        instance.priority = validated_data.get('priority', instance.priority)
        instance.active = validated_data.get('active', instance.active)
        instance.app_version = validated_data.get('app_version', instance.app_version)
        instance.device_id = validated_data.get('device_id', instance.device_id)
        instance.device_type = validated_data.get('device_type', instance.device_type)
        instance.fcm_token = validated_data.get('fcm_token', instance.fcm_token)
        instance.save()
        return instance
    
        
   
    
class PrefranceUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Preferences
        fields = ('gender', 'age_from', 'age_to', 'distance_min','distance_max', 'distance_no_limit','age_no_limit' )
        
    def update(self, instance, validated_data):
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age_from = validated_data.get('age_from', instance.age_from)
        instance.age_to = validated_data.get('age_to', instance.age_to)
        instance.distance_max = validated_data.get('distance_max', instance.distance_max)
        instance.distance_min = validated_data.get('distance_min', instance.distance_min)
        instance.distance_no_limit = validated_data.get('distance_no_limit', instance.distance_no_limit)
        instance.age_no_limit = validated_data.get('age_no_limit', instance.age_no_limit)
        instance.save()
        return instance
    
    
class UserProfileGet(serializers.ModelSerializer):
    class Meta:
        model = UserprofileImages
        fields = ('id', 'profilepics', 'is_profile', 'user_id')    
        
class UserProfileVedioGet(serializers.ModelSerializer):
    class Meta:
        model = UserprofileVideos
        fields = ('id', 'profilevideos',  'user_id')        
    
    
class UserInfoSerializer(serializers.ModelSerializer):
    
    """ User Info serializer is common serializer"""
    profilepics = UserProfileGet(many=True)
    profilevideos = UserProfileVedioGet(many=True)
    user_id    = serializers.StringRelatedField()
    name       = serializers.StringRelatedField()
    email      = serializers.StringRelatedField()
    dob        = serializers.StringRelatedField()
    gender     = serializers.StringRelatedField()
    body_type  = serializers.StringRelatedField()
    about_me   = serializers.StringRelatedField()
    height     = serializers.StringRelatedField()
    weight     = serializers.StringRelatedField()
    referral_code     = serializers.StringRelatedField()
    
    
    
    class Meta:
        model = Users
        fields = ['user_id','name','email','dob','gender','body_type','about_me','user_type','height','weight','profilepics','profilevideos','referral_code']
        
class VedioThumbnailSerializer(serializers.ModelSerializer):
    """ User Info serializer is common serializer"""
    profilevideos = UserProfileVedioGet(many=True)
    user_id    = serializers.StringRelatedField()
   
    
    
    class Meta:
        model = Users
        fields = ['user_id','profilevideos']
        
        
class HeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Height
        fields = ('id', 'height',)

class WeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weight
        fields = ('id', 'weight',)
        
class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbies
        fields = ('id', 'hobbies',)

class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ("id", "occupation")
        
        
class SuperLikeSerializer(serializers.Serializer):
    class Meta:
        models = SuperLike
        feilds = ['superlike_count']
        
class HeartSerializer(serializers.Serializer):
    class Meta:
        models = Heart
        feilds = ['heart_count']
        
from math import sin, cos, sqrt, atan2, radians, ceil

def distance_short_matrix(origin,distance):
    """
    Def : This function used to short distances(latitude,longitude) from a origin point(latitude and longitude)
    Params : origin point as a latitude and longitude and all distances list\n
    Return :sorted distances list.
    """
    lat1 = radians(float(origin['latitude']))
    lon1 = radians(float(origin['longitude']))
    R = 6373.0

    lat2 = radians(float(distance['latitude']))
    lon2 = radians(float(distance['longitude']))
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return str(ceil(R * c)) +' Km'
            



class UserlistingSerializer(serializers.ModelSerializer):
    superliked = serializers.SerializerMethodField('superlike')
    heart_to = serializers.SerializerMethodField('heart')
    
    profileimages = serializers.SerializerMethodField('profile')
    profilevedios = serializers.SerializerMethodField('vedios')  # changed
    body_type = serializers.StringRelatedField()
    age = serializers.SerializerMethodField('ages')
    about_me = serializers.SerializerMethodField('aboutuses')
    occupation = serializers.SerializerMethodField('occupations')
    distance = serializers.SerializerMethodField('distances')

    class Meta:
        model = Users
        fields = (
             'name', 'email', 'phone_no', 'age',
            'profileimages', 'occupation',"weight", "height", "body_type", "gender",
            'about_me','profilevedios','superliked','heart_to','distance')

    def distances(self,obj):
        user_id = self.context.get("user_id")
        user = Users.objects.get(id=user_id)
        origin = {'latitude':user.latitude,'longitude':user.longitude}
        return distance_short_matrix(origin,{'latitude':obj.latitude,'longitude':obj.longitude})
        

    def ages(self,obj):
        if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(age=False)).exists():
            return Users.objects.get(id=obj.pk).dob
        else:
            return None

    def aboutuses(self,obj):
        if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(aboutme=False)).exists():
            try:
                return Users.objects.get(id=obj.pk).about_me
            except:
                return None
        else:
            return None

    def occupations(self,obj):
        if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(occupation=False)).exists():
            try:
                return Users.objects.get(id=obj.pk).occupation
            except:
                return None
        else:
            return None

    def profile(self, obj):
        user_id = self.context.get("user_id")
        if user_id:
            if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(sharephotos=False)).exists():
                queryset = UserprofileImages.objects.filter(user_id=obj.pk)
                return UserProfileGet(queryset, many=True).data
            return []
        return False
    
    def vedios(self, obj):
        user_id = self.context.get("user_id")
        if user_id:
            if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(sharephotos=False)).exists():
                queryset = UserprofileVideos.objects.filter(user_id=obj.pk)
                return UserProfileVedioGet(queryset, many=True).data
            return []
        return False
    
    def superlike(self, obj):
        if SuperLike.objects.filter(superliked_id=obj.id).exists():
            return SuperLike.objects.get(superliked_id=obj.id).superlike_count
        else:
            return 0
    
    def heart(self, obj):
        if Heart.objects.filter(heart_to_id=obj.id).exists():
            return Heart.objects.get(heart_to_id=obj.id).heart_count
        else:
            return 0
        

class VediosSerializers(serializers.ModelSerializer):
    profilevedios = serializers.SerializerMethodField('vedios')  # changed
    body_type = serializers.StringRelatedField()
    latitude = serializers.StringRelatedField()
    longitude = serializers.StringRelatedField()
    age = serializers.SerializerMethodField('ages')
    about_me = serializers.SerializerMethodField('aboutuses')
    occupation = serializers.SerializerMethodField('occupations')
    class Meta:
        model = Users
        fields = (
            'user_id', 'name', 'email', 'phone_no', 'age',
             'occupation',"weight", "height", "body_type", "gender",
            'about_me','profilevedios')


    def ages(self,obj):
        if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(age=False)).exists():
            return Users.objects.get(id=obj.pk).dob
        else:
            return None

    def aboutuses(self,obj):
        if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(aboutme=False)).exists():
            try:
                return Users.objects.get(id=obj.pk).about_me
            except:
                return None
        else:
            return None

    def occupations(self,obj):
        if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(occupation=False)).exists():
            try:
                return Users.objects.get(id=obj.pk).occupation
            except:
                return None
        else:
            return None

    def vedios(self, obj):
        user_id = self.context.get("user_id")
        if user_id:
            if UserPrivacy.objects.filter(Q(user_id=obj.pk) & Q(sharephotos=False)).exists():
                queryset = UserprofileVideos.objects.filter(user_id=obj.pk)
                return UserProfileVedioGet(queryset, many=True).data
            return []
        return False
    
    
    

class UsersNotificationSerializer(serializers.ModelSerializer):
#     frnduser = LoginSerializer()
    img = serializers.SerializerMethodField('image')
    create_at=serializers.DateTimeField(format="%d-%b %I:%M:%P", required=False, read_only=True)


    class Meta:
        model = UsersNotification
        fields = ("id", "frnduser", "action", "msgtitle", "msgbody", "img", "create_at")


    def phonenumber(self, obj):
        user_id = obj.frnduser.id
        if user_id:
            if Users.objects.filter(pk=user_id).exists():
                try:
                    data = Users.objects.get(id=user_id)
                    # image = UserprofileImages.objects.get(Q(user_id=user_id) and Q(is_profile=True))
                except:
                    return
                if data:
                    fullname = data.phone_no
                    # img = image.profilepics.url
                return '{}'.format(fullname)

    def image(self, obj):
        user_id = obj.frnduser.id
        if user_id:
            if UserprofileImages.objects.filter(user_id=user_id, is_profile=True).exists():
                try:
                    u = UserprofileImages.objects.get(user_id=user_id, is_profile=True)
                except:
                    return ""
                if u:
                    img = u.profilepics.url
                    return img
                
                
# class GetLikedByMeSerializer(serializers.ModelSerializer):
#     liked_to = UserlistingSerializer()
#     class Meta:
#         model = Like
#         fields = ("liked_to", "likes_at",)
