from django.db import models
from userprofile.models import Users
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import datetime, timedelta


def expire_date_for_basic():
    return datetime.now()+timedelta(days=7)

class Plans(models.Model):
    name = models.CharField(max_length=100)
    plan_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Accessories(models.Model):
    name = models.CharField(max_length=100)
    accessories_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name    


class AccessoriesDetails(models.Model):
    accessories = models.ForeignKey(Accessories, on_delete=models.CASCADE, blank=False)
    price = models.DecimalField(verbose_name="Accessories Price", max_digits=6, decimal_places=2)
    validity = models.CharField(blank=False, max_length=10)
    description = models.TextField()
    
    remaining_hi         = models.IntegerField(default=0, verbose_name="Number of Hi")
    remaining_hearts     = models.IntegerField(default=0, verbose_name="Number of Hearts")
    remaining_boosts     = models.IntegerField(default=0, verbose_name="Number of Boosts")
    remaining_talktime   = models.IntegerField(default=0, verbose_name="Number of Talk Time")
    remaining_superlikes = models.IntegerField(default=0, verbose_name="Number of Super Like")
    
    wallet_percentage   = models.FloatField(default=0.0)
    discount_percentage = models.FloatField(default=0.0)
    def __str__(self):
        return "{} - {}".format(self.accessories.name, self.validity)


class PlanDetails(models.Model):
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE, blank=False, related_name="plandetail")
    price = models.DecimalField(verbose_name="Plan Price", max_digits=6, decimal_places=2)
    validity = models.IntegerField(default=0)
    description = models.TextField()
    
    hi         = models.IntegerField(default=0, verbose_name="Number of Hi")
    hearts     = models.IntegerField(default=0, verbose_name="Number of Hearts")
    likes         = models.IntegerField(default=0, verbose_name="Number of Likes")
    boosts     = models.IntegerField(default=0, verbose_name="Number of Boosts")
    talktime   = models.IntegerField(default=0, verbose_name="Talk Time Minutes")
    superlikes = models.IntegerField(default=0, verbose_name="Number of Super Like")

    wallet_percentage = models.FloatField(default=0.0)
    discount_percentage = models.FloatField(default=0.0)
    
    video_enabled         = models.BooleanField(default=False)
    audio_enabled         = models.BooleanField(default=False)
    sees_control          = models.BooleanField(default=False)
    interested_profile    = models.BooleanField(default=False)
    hide_ads              = models.BooleanField(default=False)
    profile_control       = models.BooleanField(default=False)
    stickers              = models.BooleanField(default=False)
    scrach_enable         = models.BooleanField(default=False)
    e_greetings_enable    = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {}".format(self.plan.name, self.validity)

class UserDailyDose(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    plan = models.ForeignKey(PlanDetails, on_delete=models.CASCADE, null=True)
    plan_name = models.CharField(default='Basic', max_length=50, null=True)
    
    remaining_hi         = models.IntegerField(default=5)
    remaining_likes      = models.IntegerField(default=100)
    remaining_hearts     = models.IntegerField(default=5)
    remaining_boosts     = models.IntegerField(default=5)
    remaining_talktime   = models.IntegerField(default=5)
    remaining_superlikes = models.IntegerField(default=5)
    
    is_active      = models.BooleanField(default=True)
    is_expired     = models.BooleanField(default=False)
    plan_expire_at = models.DateTimeField(null=True, blank=True)
    payment_token = models.CharField(max_length=60,blank=True)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.name
    
@receiver(post_save, sender=Users)
def update_user_daily_dose(sender, instance, created, **kwargs):
    if created:
        UserDailyDose.objects.create(user=instance, plan_id=1,plan_expire_at=expire_date_for_basic()) 
     
    
class PlanPurchedByUser(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    plan_id = models.CharField(max_length=10, null=True, blank=True)
    plan_name = models.CharField(max_length=30, null=True, blank=True)
    accessories_id = models.CharField(max_length=10,null=True, blank=True)
    accessories_name = models.CharField(max_length=30,null=True, blank=True)
    paytm_txn_id = models.CharField(max_length=40,null=True, blank=True)
    order_id    = models.CharField(max_length=30,unique=True)
    paytm_amount       = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    cashback_amount    = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    discount_amount    = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    wallet_amount      = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    discount_amount    = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    plan_price_amount  = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    
    plan_purched_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.user.user_id
    
class PurchaseRequest(models.Model):   
    user             = models.ForeignKey(Users, on_delete=models.CASCADE)
    plan_id          = models.CharField(max_length=10, null=True, blank=True)
    plan_name        = models.CharField(max_length=30, null=True, blank=True)
    accessories_id   = models.CharField(max_length=10, null=True, blank=True)
    accessories_name = models.CharField(max_length=30, null=True, blank=True)
    order_id    = models.CharField(max_length=30, unique=True)
    
    paytm_amount       = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    cashback_amount    = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    discount_amount    = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    wallet_amount      = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    discount_amount    = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    plan_price_amount  = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)
    
    plan_request_at = models.DateTimeField(auto_now_add=True)
     
    def __unicode__(self):
        return self.user.user_id
#     


class Wallet(models.Model):
    user            = models.OneToOneField(Users, on_delete=models.CASCADE)
    wallet_amount   = models.DecimalField(default=1000, decimal_places=2, max_digits=6)
    referral_amount = models.DecimalField(default=0,  decimal_places=2, max_digits=6)
    last_updated    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name


@receiver(post_save, sender=Users)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
    instance.wallet.save()

  
    
    
class PaytmPaymentStatus(models.Model):
    order_id       = models.CharField(max_length=30,unique=True)
    txn_id         = models.CharField(max_length=100)
    txn_type       = models.CharField(max_length=30, blank=True)
    bank_txn_id    = models.CharField(max_length=100,blank=True)
    bank_name      = models.CharField(max_length=50, blank=True)
    resp_code      = models.IntegerField()
    payment_mode   = models.CharField(max_length=10,blank=True)
    gatway_name    = models.CharField( max_length=30,blank=True)
    mid            = models.CharField(max_length=100,blank=True)
    resp_msg       = models.TextField(max_length=250)
    txn_amount     = models.DecimalField(max_length=10,max_digits=6,decimal_places=2)
    refund_amount  = models.DecimalField(max_length=10,max_digits=6,decimal_places=2)
    status         = models.CharField(max_length=12)
    txn_date       = models.DateTimeField(blank=True)
     
 
    def __unicode__(self):
        return self.txn_id
    