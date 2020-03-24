from django.contrib import admin
from cheatingdash.models import PaytmHistory
from cheatingdash.models import StatusHistory

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