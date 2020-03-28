from django.contrib import admin
from cheatingdash.models import PaytmHistory
from cheatingdash.models import StatusHistory,UserProfile,userSubscriptions

# Register your models here.
class PaytmHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'ORDERID','MID','TXNDATE','BANKNAME', 'GATEWAYNAME','TXNAMOUNT', 'STATUS')
    list_filter = ('TXNDATE','BANKNAME' )
    date_hierarchy = ('TXNDATE')
    search_fields=('BANKNAME',)


admin.site.register(PaytmHistory, PaytmHistoryAdmin)

class StatusHistoryAdmin(admin.ModelAdmin):
    list_display = ( 'ORDERID','MID','TXNTYPE','TXNDATE','BANKNAME', 'GATEWAYNAME','PAYMENTMODE','TXNAMOUNT', 'STATUS')


admin.site.register(StatusHistory, StatusHistoryAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','age','phone','address' )


admin.site.register(UserProfile, UserProfileAdmin)

class userSubscriptionsAdmin(admin.ModelAdmin):
    list_display = ('user','SubsplanName','price','status' )


admin.site.register(userSubscriptions, userSubscriptionsAdmin)