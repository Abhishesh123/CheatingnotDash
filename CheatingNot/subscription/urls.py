from django.urls import path
from subscription import views



 
urlpatterns = [
    path('get_all_plans', views.AllPlans.as_view()),
    path('get_my_plan', views.UserSubscription.as_view(), name='Subscription'), 
    path('get_paid_amount', views.GetPaidAmount.as_view(), name='User Subscription'),
    path('enroll_user_subscription', views.EnrollUserSubscription.as_view(), name='User Subscription'),
    path('enroll_user_accessories', views.EnrollUserAccessories.as_view(), name='Accessories Subscription'),
    path('startboost/<user_id>', views.StartBoost.as_view(), name='start boost'), 
#     path('notification/<int:pk>', UsersNotificationView.as_view(), name='usernotification'),
#     path('dailydose-cronjob', UpdateUserDailyDose.as_view(), name='updateuserdailydose')
]