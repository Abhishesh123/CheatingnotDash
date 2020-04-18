from django.contrib import admin
from cheatingdash.models import PaytmHistory
from cheatingdash.models import StatusHistory,UserProfile,userSubscriptions,Matchprofile,orderManagement,superPlans,singlePlans

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

class MatchprofileAdmin(admin.ModelAdmin):
    list_display = ('matchid','user1id','user2id','status' )


admin.site.register(Matchprofile, MatchprofileAdmin)
class orderManagementAdmin(admin.ModelAdmin):
	list_display=('user','planName','price','status' )

admin.site.register(orderManagement,orderManagementAdmin)
class singlePlansAdmin(admin.ModelAdmin):
	list_display=('title','description' )

admin.site.register(singlePlans,singlePlansAdmin)

class superPlansAdmin(admin.ModelAdmin):
	list_display=('planName','durationMonth','price' )

admin.site.register(superPlans,superPlansAdmin)
