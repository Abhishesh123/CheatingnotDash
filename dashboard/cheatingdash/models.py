from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,blank=True)
    priority = models.CharField(max_length=30,blank=True)

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