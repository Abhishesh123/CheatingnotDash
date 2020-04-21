from rest_framework import serializers
from subscription.models import UserDailyDose,AccessoriesDetails, PlanDetails,Plans
from datetime import datetime, timedelta


#  plan = models.ForeignKey(Plans, on_delete=models.CASCADE, blank=False, related_name="plandetail")
#     price = models.DecimalField(verbose_name="Plan Price", max_digits=6, decimal_places=2)
#     validity = models.CharField(blank=False, max_length=10)
#     description = models.TextField()
#     
#     hi         = models.IntegerField(default=0, verbose_name="Number of Hi")
#     likes      = models.IntegerField(default=0, verbose_name="Number of Likes")
#     hearts     = models.IntegerField(default=0, verbose_name="Number of Hearts")
#     boosts     = models.IntegerField(default=0, verbose_name="Number of Boosts")
#     talktime   = models.IntegerField(default=0, verbose_name="Talk Time Minutes")
#     superlikes = models.IntegerField(default=0, verbose_name="Number of Super Like")
# 
#     wallet_percentage = models.FloatField(default=0.0)
#     discount_percentage = models.FloatField(default=0.0)
#     
#     video_enabled         = models.BooleanField(default=False)
#     audio_enabled         = models.BooleanField(default=False)
#     sees_control          = models.BooleanField(default=False)
#     interested_profile    = models.BooleanField(default=False)
#     hide_ads              = models.BooleanField(default=False)
#     profile_control       = models.BooleanField(default=False)
#     stickers              = models.BooleanField(default=False)
#     scrach_enable         = models.BooleanField(default=False)
#     e_greetings_enable    = models.BooleanField(default=False)

class PlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDetails
        fields = (
            "price", "id", "validity", "description", "hi",
            'likes', 'hearts', 'boosts','talktime','superlikes',
            "video_enabled", "audio_enabled",
             "stickers", "sees_control", "interested_profile", "hide_ads", "profile_control",'scrach_enable','e_greetings_enable')


class PlanSerializer(serializers.ModelSerializer):
    plandetail = PlanDetailSerializer(many=True)
    class Meta:
        model = Plans
        fields = '__all__'
        
        
class UserDoseSerializer(serializers.ModelSerializer):
    plan = PlanDetailSerializer()

    class Meta:
        model = UserDailyDose
        fields = '__all__'
        


class AccessoriesUpdateSerializer(serializers.ModelSerializer):
    remaining_hi = serializers.SerializerMethodField('get_remaining_hi')
    remaining_likes = serializers.SerializerMethodField('get_remaining_likes')
    remaining_boosts = serializers.SerializerMethodField('get_remaining_boosts')
    remaining_boosts = serializers.SerializerMethodField('get_remaining_hearts')
    remaining_talktime = serializers.SerializerMethodField('get_remaining_talktime')
    remaining_superlikes = serializers.SerializerMethodField('get_remaining_superlikes')
    
    class Meta:
        model = UserDailyDose
        fields = ['remaining_hi', 'remaining_likes','remaining_boosts','remaining_talktime','remaining_superlikes','remaining_hearts']
        
   
        
    def update(self, instance, validated_data):
        instance.remaining_hi = validated_data.get('remaining_hi', instance.remaining_hi)
        instance.remaining_likes = validated_data.get('remaining_likes', instance.remaining_likes)
        instance.remaining_boosts = validated_data.get('remaining_boosts', instance.remaining_boosts)
        instance.remaining_talktime = validated_data.get('remaining_talktime', instance.remaining_talktime)
        instance.remaining_superlikes = validated_data.get('remaining_superlikes', instance.remaining_superlikes)
        instance.remaining_hearts = validated_data.get('remaining_hearts', instance.remaining_hearts)
        instance.save()
        return instance    
    
    def get_remaining_hi(self, obj):
        return int(obj.hi)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).hi)
    
    def get_remaining_likes(self, obj):
        return int(obj.likes)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).likes)
    
    def get_remaining_boost(self, obj):
        return int(obj.boost)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).boost)
    
    def get_remaining_superlikes(self, obj):
        return int(obj.superlike)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).superlike)
    
    def get_remaining_talktime(self, obj):
        return int(obj.talktime)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).talktime)
    
    def get_remaining_hearts(self, obj):
        return int(obj.hearts)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).hearts)
    
    
#      userdose.plan_name = plan_details.name
#             userdose.remaining_boosts = int(userdose.remaining_boosts)+int(plan_details.boosts)
#             userdose.remaining_superlikes = int(userdose.remaining_superlikes)+int(plan_details.superlike)
#             userdose.remaining_likes = int(userdose.remaining_likes)+int(plan_details.like)
#             userdose.remaining_talktime = int(userdose.remaining_talktime)+int(plan_details.talktime)
#             userdose.remaining_hi = int(userdose.remaining_hi)+int(plan_details.hi)
#             userdose.remaining_hearts = int(userdose.remaining_hi)+int(plan_details.hearts)
#             userdose.is_active = True
#             userdose.is_expired = False
#             userdose.plan_expire_at = datetime.now() + timedelta(days=int(plan_details.validity))
#             userdose.save()

class UserDoseUpdateSerializer(serializers.ModelSerializer):
    plan_id = serializers.SerializerMethodField('get_plan_id')
    plan_name = serializers.SerializerMethodField('get_plan_name')
    remaining_hi = serializers.SerializerMethodField('get_remaining_hi')
    remaining_likes = serializers.SerializerMethodField('get_remaining_likes')
    remaining_boosts = serializers.SerializerMethodField('get_remaining_boosts')
    remaining_boosts = serializers.SerializerMethodField('get_remaining_hearts')
    remaining_talktime = serializers.SerializerMethodField('get_remaining_talktime')
    remaining_superlikes = serializers.SerializerMethodField('get_remaining_superlikes')
    is_expired = serializers.SerializerMethodField('get_is_expired')
    is_active = serializers.SerializerMethodField('get_is_active')
    plan_expire_at = serializers.SerializerMethodField('get_expire_date')
    
    class Meta:
        model = UserDailyDose
        fields = '__all__'
        
    def get_remaining_hi(self, obj):
        return int(obj.hi)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).hi)
    
    def get_remaining_likes(self, obj):
        return int(obj.likes)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).likes)
    
    def get_remaining_boost(self, obj):
        return int(obj.boost)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).boost)
    
    def get_remaining_superlikes(self, obj):
        return int(obj.superlike)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).superlike)
    
    def get_remaining_talktime(self, obj):
        return int(obj.talktime)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).talktime)
    
    def get_remaining_hearts(self, obj):
        return int(obj.hearts)+ int(AccessoriesDetails.objects.get(accessories_id=obj.id).hearts)    
    
    def get_is_expired(self, obj):
        return  False
        
    def get_is_active(self, obj):
        return  True
    
    def get_expire_date(self,obj):
        obj.plan_expire_at = datetime.now() + timedelta(days=int(PlanDetails.objects.get(plan_id=obj.id).validity))
        
    def update(self, instance, validated_data):
        instance.plan_id = validated_data.get('plan_id', instance.plan_id)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.remaining_hi = validated_data.get('remaining_hi', instance.remaining_hi)
        instance.remaining_likes = validated_data.get('remaining_likes', instance.remaining_likes)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        instance.plan_name = validated_data.get('plan_name', instance.plan_name)
        
        instance.save()
        return instance        
        
        
        
        