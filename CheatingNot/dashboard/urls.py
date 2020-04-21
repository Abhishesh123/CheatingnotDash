from django.urls import path
from dashboard import views
app_name = "dashboard"

from . import views

urlpatterns = [
    path('', views.Index),
    path('userList/',views.userList,name='userList'),
    path('Detailsuser/<uuid:id>',views.Detailsuser,name='Detailsuser'),
    path('userUpdate/<uuid:id>', views.userUpdate, name='userUpdate'),
    path('blockuser/<uuid:id>',views.blockuser,name='blockuser'),
    path('unblockuser/<uuid:id>',views.unblockuser,name='unblockuser'),
    path('blockUserslist/',views.blockUserslist,name='blockUserslist'),
    path('searchUser/',views.searchUser,name="searchUser"),
    path('planpurchedbyuser/',views.planpurchedbyuser,name="planpurchedbyuser"),
    path('planpurchedbyuserdetail/<int:id>',views.planpurchedbyuserDetails,name="planpurchedbyuserDetails")

]