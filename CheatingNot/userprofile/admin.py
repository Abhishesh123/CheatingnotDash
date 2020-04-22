from django.contrib import admin
from userprofile.models import *

class OccupationAdmin(admin.ModelAdmin):
    pass
admin.site.register(Occupation,OccupationAdmin)


class HobbiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hobbies,HobbiesAdmin)


class OTPAdmin(admin.ModelAdmin):
    pass
admin.site.register(OTP,OTPAdmin)


class AnonymousAdmin(admin.ModelAdmin):
    pass
admin.site.register(Anonymous,AnonymousAdmin)


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users,UserAdmin)


class HeightAdmin(admin.ModelAdmin):
    pass
admin.site.register(Height,HeightAdmin)


class WeightAdmin(admin.ModelAdmin):
    pass
admin.site.register(Weight,WeightAdmin)

class PushNotificationMsgAdmin(admin.ModelAdmin):
    pass
admin.site.register(PushNotificationMsg,PushNotificationMsgAdmin)


class DiscountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Discount,DiscountAdmin)
class MatchAdmin(admin.ModelAdmin):
	pass
admin.site.register(Match,MatchAdmin)



















# Register your models here.
