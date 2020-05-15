from django.urls import path
from dashboard import views
app_name = "dashboard"

from . import views

urlpatterns = [
    path('', views.Index),
    path('login', views.Login),
    path('login', views.Logout, name='Logout'),
    path('userList/',views.userList,name='userList'),
    path('Detailsuser/<uuid:id>',views.Detailsuser,name='Detailsuser'),
    path('userUpdate/<uuid:id>', views.userUpdate, name='userUpdate'),
    path('blockuser/<uuid:id>',views.blockuser,name='blockuser'),
    path('unblockuser/<uuid:id>',views.unblockuser,name='unblockuser'),
    path('blockUserslist/',views.blockUserslist,name='blockUserslist'),
    path('searchUser/',views.searchUser,name="searchUser"),
    path('planpurchedbyuser/',views.planpurchedbyuser,name="planpurchedbyuser"),
    path('planpurchedbyuserdetail/<int:id>',views.planpurchedbyuserDetails,name="planpurchedbyuserDetails"),
    path('matchedprofiles/',views.matchedprofiles,name='matchedprofiles'),
    path('DeleteMatchprofiles/<int:id>',views.Matchprofiles,name='Matchprofiles'),
    path('Reported/',views.Reported,name="Reported"),
    path('paytmpaymentStatus/',views.paytmpaymentStatus,name='paytmpaymentStatus'),
    path('ordermanagement/',views.ordermanagement,name="ordermanagement"),
    path('ordermanagementDetails/<int:id>',views.ordermanagementDetails,name="ordermanagementDetails"),
    path('orderAnalytics/',views.orderAnalytics,name="orderAnalytics"),
    path('deleteReported/<int:id>',views.deleteReported,name="deleteReported"),
    path('userListCSV/',views.userListCSV,name='userListCSV'),
    path('datefilter/',views.datefilter,name="datefilter"),
    path('Access/',views.Access,name="Access"),
    path('AddAccessories/',views.AddAccessories,name='AddAccessories'),
    path('DetailsAccessories/',views.DetailsAccessories,name='DetailsAccessories'),
    path('AddAccessoriesdetails/',views.AddAccessoriesdetails,name='AddAccessoriesdetails'),
    path('userAnalytics/',views.userAnalytics,name="userAnalytics"),
    path('subsAnalytics/',views.subsAnalytics,name="subsAnalytics"),
    path('Paymentdetail/<int:id>', views.Paymentdetail, name='Paymentdetail_id'),
    path('searchOrder/',views.searchOrder,name="searchOrder"),
    path('OrderCSV/',views.OrderCSV,name="OrderCSV"),
    path('wallet/',views.wallet,name='wallet'),
    path('UserdailyDose/',views.UserdailyDose,name="UserdailyDose"),

]