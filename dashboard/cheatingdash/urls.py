from django.urls import path
from . import views



urlpatterns = [
    path('', views.Index),
    path('userlist', views.userList, name='userList'),
    path('user', views.searchUser, name='searchUser'),
    path('login', views.Login),
    path('logout', views.Logout, name='Logout'),
    path('block/<int:id>', views.Block, name='Block'),
    path('unblock/<int:id>', views.unBlock, name='unBlock'),
    path('block-users/', views.blockUsers, name='blockUsers'),
    path('details/<int:id>', views.Details, name='Details'),
    path('edit/<int:id>', views.Edit, name='Edit'),
    path('update/<int:id>', views.Update, name='Update'),
    path('contact', views.ContactMe, name='ContactMe'),
    path('send-sms', views.sendSMS, name='sendSMS'),


    #employee model
    path('emp', views.empList, name='empList'),
    path('emp-create', views.create, name='create'),
    path('emp-update/<int:id>', views.empupdate, name='empupdate'),
    # path('details', views.Details, name='Details'),
]