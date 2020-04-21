from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from billiard.five import monotonic

class Occupation(models.Model):
    occupation = models.CharField(max_length=30) 
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.occupation) if self.occupation else ''
    
# Hobbies table or interest table
class Hobbies(models.Model):
    """ User hobbies, likes, interest """
    hobbies = models.CharField(null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hobbies if self.hobbies else ''    

    
# Hobbies table or interest table
class Height(models.Model):
    """ User hobbies, likes, interest """
    height = models.CharField(blank=True, max_length=20,verbose_name='Height in Cm')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.height if self.height else ''
# Hobbies table or interest table
class Weight(models.Model):
    """ User hobbies, likes, interest """
    weight = models.CharField(blank=True, max_length=20,verbose_name="Weight in Kg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return self.weight if self.weight else ''

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=30,blank=True)
    email  = models.EmailField(blank=True)
    phone_no = models.CharField(max_length=15,blank=True)
    country_code = models.CharField(max_length=4,blank=True,null=True)
    
    dob = models.DateField(blank=True)
    gender = models.CharField(max_length=6,blank=True)
    body_type = models.CharField(max_length=10,blank=True)
    about_me = models.CharField(max_length=100,blank=True)
    user_type = models.CharField(max_length=20,blank=True)
    occupation = models.CharField(max_length=30, blank=True)
    height = models.CharField(blank=True, max_length=20)
    weight = models.CharField(blank=True, max_length=10)
    latitude  = models.FloatField(blank=True,default=0.0)
    longitude  = models.FloatField(blank=True,default=0.0)
    distance  = models.FloatField(default=0.0)
    referral_code  = models.CharField(max_length=10)
    
    priority = models.IntegerField(default=0,blank=True)
    profile_verified = models.BooleanField(default=False)
    active  = models.BooleanField(default=False)
    staff  = models.BooleanField(default=False)
    
    app_version = models.FloatField(null=True, blank=True)
    device_id = models.CharField(max_length=30,null=True, blank=True)
    device_type = models.CharField(max_length=10,null=True, blank=True)
    fcm_token = models.CharField(max_length=200,null=True, blank=True)
    profile_complete_percentage = models.IntegerField(blank=True,default=0)
    profile_update_percentage = models.IntegerField(default=0)
    last_login = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
      

    
class Anonymous(models.Model):
    phone_no = models.CharField(max_length=12,null=True, blank=True)
    country_code = models.CharField(max_length=4, null=True, blank=True)  
    email = models.EmailField(null=True, blank=True)
    auth_token = models.CharField(max_length=100)
    app_version = models.FloatField()
    device_id = models.CharField(max_length=30)
    device_type = models.CharField(max_length=10,null=True)#ios/android
    fcm_token = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.phone_no if self.phone_no else self.email
    
    
    
class OTP(models.Model):
    user = models.OneToOneField(Anonymous, on_delete=models.CASCADE)
    otp = models.CharField(max_length=10, null=True, blank=True)
    otp_expire_at = models.DateTimeField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone_no
    
class UserprofileImages(models.Model):
    """  images for particular user """
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='profilepics')
    profilepics = models.ImageField(upload_to='profiles')
    is_profile = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name

    
class UserprofileVideos(models.Model):
    """  images for particular user """
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='profilevideos')
    profilevideos = models.ImageField(upload_to='profiles_vedios')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name    
    

    
    
class UserAuth(models.Model):
    """  images for particular user """
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.user.name  
    
class Preferences(models.Model):
    """ user setting for filtration """
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age_from = models.IntegerField(null=True, blank=True)
    age_to = models.IntegerField(null=True, blank=True)
    distance_min = models.CharField(null=True, blank=True, max_length=10)
    distance_max = models.CharField(null=True, blank=True, max_length=10)
    distance_no_limit = models.BooleanField(default=False)
    preferences_update_percentage = models.IntegerField(default=0)
    age_no_limit = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
    
# # signal for creation of user settings
@receiver(post_save, sender=Users)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.gender == "Male":
            gender = "Female"
        elif instance.gender == "Female":
            gender = "Male"
        else:
            gender = "Both"
        Preferences.objects.create(user=instance, age_from=18, age_to=50, distance_max=50,gender=gender)
    instance.preferences.save()
     
    
    
class UserPrivacy(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    age = models.BooleanField(default=False)
    showme = models.BooleanField(default=False)
    aboutme = models.BooleanField(default=False)
    sharephotos = models.BooleanField(default=False)
    occupation = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.name
    
@receiver(post_save, sender=Users)
def update_user_privacy(sender, instance, created, **kwargs):
    if created:
        UserPrivacy.objects.create(user=instance)
    instance.userprivacy.save()    
    
    
class Nopes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="user")
    nope = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="nope")
    create_at = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.user.name
 
class Like(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="liked_by")
    liked = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="liked")
    create_at = models.DateTimeField(auto_now_add=True)
    
  
    def __str__(self):
        return self.user.name

class Hi(models.Model):
    user  = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="hi_by")
    hi_to = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="hi_to")
    hi_count = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.user.name

class SuperLike(models.Model):
    user           = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="superlike_by")
    superliked = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="superliked")
    superlike_count = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.user.name
     
class Heart(models.Model):
    user       = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="heaet_by")
    heart_to = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="heart_to")
    heart_count = models.IntegerField(default=0)
    create_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.user.name
     
class Match(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,related_name="match_by")
    matches = models.ManyToManyField(Users, blank=True,related_name="matches")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.user.name
    
class Block(models.Model):
    """ check Block user """
    blocked    = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="blocked")
    blocked_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="blocked_by")
    blocked_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.name
    


class Reports(models.Model):
    """ check reported user """
    reported = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="reported")
    reported_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="reported_by")
    reason = models.CharField(max_length=256)
    report_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.name
    
    
    
notification_choices = ((1, 'hi'), (2, 'like'), (3, 'superlike'),(4,'heart'),(5,'match'),(6,'referral'))


class PushNotificationMsg(models.Model):
    notification_type = models.IntegerField(blank=True, choices=notification_choices)
    msg_title = models.CharField(max_length=60,blank=True)
    msg_body = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.msg_body

    
    
class UsersNotification(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender')
    friend_user  = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='receiver')
    img          = models.CharField(max_length=200, null=True, blank=True)
    action       = models.CharField(max_length=200, null=True, blank=True)
    msg_title    = models.CharField(max_length=200, null=True, blank=True)
    msg_body     = models.CharField(max_length=200, null=True, blank=True)
    create_at    = models.DateTimeField(auto_now=True)
    updated_at  = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.user.name
    
    
class Discount(models.Model):   
    cashback_percentage = models.DecimalField(max_length=10,max_digits=6,decimal_places=2)
    referral_amount     = models.DecimalField(max_length=10,max_digits=6,decimal_places=2)
     
      
    def __str__(self):
        return str(self.cashback_percentage)
  


    
  
    
    