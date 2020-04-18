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
    path('userListCSV/',views.userListCSV,name='userListCSV'),
    path('search/', views.searchUser, name='searchUser'),
    path('datefilter/',views.datefilter,name="datefilter"),
    path('userSubscription/',views.userSubscription,name="userSubscriptions"),
    path('userSubscriptionDetails/<int:id>',views.userSubscriptionDetails,name="userSubscriptionDetails"),
    path('userSubscriptionsCSV/',views.userSubscriptionsCSV,name="userSubscriptionsCSV"),
    path('searchSubscriptions/',views.searchSubscriptions,name="searchSubscriptions"),
    path('salescharts/',views.salescharts,name="salescharts"),
    path('resetpassword/',views.resetpassword,name="resetpassword"),
    path('sendlink/',views.sendlink,name="sendlink"),
    path('Deleteuser/<int:id>',views.Deleteuser,name="Deleteuser"),
    path('Detailsuser/<int:id>',views.Detailsuser,name="Detailsuser"),
    path('send_otp/',views.send_otp ,name="send_otp") ,
    path('userUpdate/<int:id>', views.userUpdate, name='userUpdate'),
    path('userAnalytics/',views.userAnalytics,name='userAnalytics'),
    path('get_all_logged_in_users/',views.get_all_logged_in_users,name='get_all_logged_in_users'),
    path('alllogin/',views.alllogin,name="alllogin"),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('unblockuser/<int:id>',views.unblockuser,name='unblockuser'),
    path('blockUserslist/',views.blockUserslist,name='blockUserslist'),
    path('matchedprofiles/',views.matchedprofiles,name='matchedprofiles'),
    path('Matchprofiles/<int:id>',views.Matchprofiles,name='Matchprofiles'),
    path('ordermanagement/',views.ordermanagement,name="ordermanagement"),
    path('userSubscription/freeplan/',views.freeplan,name="freeplan"),
    path('userSubscription/superPlan/',views.superPlan,name="superPlans"),
    path('userSubscription/singlePlan/',views.singlePlan,name='singlePlan')


]
