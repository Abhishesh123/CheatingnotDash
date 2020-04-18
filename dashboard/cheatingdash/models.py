from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    address = models.TextField( blank=True, null=True)
    age=models.CharField(max_length=4,null=True, blank=True)
    phone=models.CharField(max_length=11,null=True, blank=True)
    city=models.CharField(max_length=40,null=True, blank=True)
    is_active = models.BooleanField( default=True) 
    create_at = models.DateTimeField(auto_now_add=True)



    def __unicode__(self):
        return self.user.username

class PaytmHistory(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE,related_name='rel_payment_paytm')
    ORDERID = models.CharField('ORDER ID', max_length=300)
    TXNDATE = models.DateTimeField('TXN DATE', auto_now_add=True)
    TXNID = models.CharField('TXN ID',max_length=300,null=True, blank=True)
    BANKTXNID = models.CharField('BANK TXN ID',max_length=300, null=True, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
    RESPCODE = models.IntegerField('RESP CODE',)
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
    CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
    MID = models.CharField(max_length=100,null=True, blank=True)
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNAMOUNT = models.FloatField('TXN AMOUNT', max_length=250)
    STATUS = models.CharField('STATUS', max_length=12)

    class Meta:
        app_label = 'cheatingdash'

    def __unicode__(self):
        return self.STATUS

class StatusHistory(models.Model):
   
    ORDERID = models.CharField('ORDER ID', max_length=300)
    TXNDATE = models.DateTimeField('TXN DATE', auto_now_add=True)
    TXNID = models.CharField('TXN ID',max_length=300,null=True, blank=True)
    TXNTYPE=models.CharField('TXNTYPE',max_length=300,null=True, blank=True)
    BANKTXNID = models.CharField('BANK TXN ID',max_length=300, null=True, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=50, null=True, blank=True)
    RESPCODE = models.IntegerField('RESP CODE',)
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=30, null=True, blank=True)
    MID = models.CharField(max_length=100,null=True, blank=True)
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNAMOUNT = models.FloatField('TXN AMOUNT', max_length=250)
    REFUNDAMT=models.FloatField('REFUNDAMT', max_length=250)
    STATUS = models.CharField('STATUS', max_length=12)

    class Meta:
        app_label = 'cheatingdash'

    def __unicode__(self):
        return self.STATUS
class userSubscriptions(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    SubsplanName=models.CharField(max_length=4,null=True, blank=True)
    durationMonth= models.IntegerField()
    price= models.IntegerField()
    BoostCount =  models.IntegerField()
    BoostMinute = models.IntegerField()
    SuperLikeCount=models.IntegerField()
    status  = models.IntegerField(default=0, choices=STATUS)
    subsdate = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'cheatingdash'

    def __unicode__(self):
        return self.status
class AllLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    date= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.user) + ': ' + str(self.date)
class Matchprofile(models.Model):
    INACTIVE = 0
    ACTIVE = 1
    STATUS = (
        (INACTIVE, _('Inactive')),
        (ACTIVE, _('Active')),
    )
    matchid=models.IntegerField()
    user1id=models.IntegerField()
    user2id=models.IntegerField()
    status  = models.IntegerField(default=0, choices=STATUS)
    matched_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'cheatingdash'

    def __unicode__(self):
        return self.status


class orderManagement(models.Model):

        INACTIVE = 0
        ACTIVE = 1
        STATUS = (
            (INACTIVE, _('Inactive')),
            (ACTIVE, _('Active')),
        )
        subsid= models.OneToOneField(userSubscriptions, on_delete=models.CASCADE,null=True, blank=True)
        user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
        planName=models.CharField(max_length=4,null=True, blank=True)
        durationMonth= models.IntegerField()
        price= models.IntegerField()
        BoostCount =  models.IntegerField()
        BoostMinute = models.IntegerField()
        SuperLikeCount=models.IntegerField()
        status  = models.IntegerField(default=0, choices=STATUS)
        created_at=models.DateTimeField(auto_now_add=True)
        class Meta:
            app_label = 'cheatingdash'

        def __unicode__(self):
            return self.status

class superPlans(models.Model):
    planName=models.CharField(max_length=4,null=True, blank=True)
    durationMonth= models.IntegerField()
    price= models.IntegerField()


    class Meta:
        app_label = 'cheatingdash'

    def __unicode__(self):
        return self.price
class singlePlans(models.Model):
    title=models.CharField(max_length=100,null=True, blank=True)
    description=models.CharField(max_length=100,null=True, blank=True)
    Ty=models.CharField(max_length=100,null=True, blank=True)
    


    class Meta:
        app_label = 'cheatingdash'

    def __unicode__(self):
        return self.Type


