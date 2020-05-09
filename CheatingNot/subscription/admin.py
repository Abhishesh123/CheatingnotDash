from django.contrib import admin
from subscription.models import *



class PlansAdmin(admin.ModelAdmin):
    pass
admin.site.register(Plans, PlansAdmin)


class PlanDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PlanDetails,PlanDetailsAdmin)


class AccessoriesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Accessories, AccessoriesAdmin)


class AccessoriesDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(AccessoriesDetails,AccessoriesDetailsAdmin)

class UserDailyDoseAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserDailyDose, UserDailyDoseAdmin)

class PlanPurchedByUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(PlanPurchedByUser, PlanPurchedByUserAdmin)

class PaytmPaymentStatusAdmin(admin.ModelAdmin):
    pass
admin.site.register(PaytmPaymentStatus, PaytmPaymentStatusAdmin)


