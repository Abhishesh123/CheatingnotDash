from django.urls import path
from cheatingdash import views
app_name = "cheatingdash"

from . import views


urlpatterns = [
    path('', views.Index),
    path('login', views.Login),
    path('login', views.Logout, name='Logout'),
    path('paymentStatus/',views.paymentStatus,name='paymentStatus'),
    path('StatusHistorys/',views.StatusHistorys,name='StatusHistory'),
    path('PaydetailStatus/<int:id>', views.PaydetailStatus, name='PaydetailStatus'),
    path('Paymentdetail/<int:id>', views.Paymentdetail, name='Paymentdetail_id'),
    path('userList/',views.userList,name='userList'),
    path('search/', views.searchUser, name='searchUser'),
    path('datefilter/',views.datefilter,name="datefilter"),
    path('userSubscription/',views.userSubscription,name="userSubscriptions"),
    path('userSubscriptionDetails/<int:id>',views.userSubscriptionDetails,name="userSubscriptionDetails"),
    path('userSubscriptionsCSV/',views.userSubscriptionsCSV,name="userSubscriptionsCSV"),
    path('searchSubscriptions/',views.searchSubscriptions,name="searchSubscriptions")

]
