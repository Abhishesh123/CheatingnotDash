from django.urls import path
from . import views



urlpatterns = [
    path('', views.Index),
    path('userlist', views.userList, name='userList'),
    path('user', views.searchUser, name='searchUser'),
    path('login', views.Login),
    path('logout', views.Logout, name='Logout'),
    path('delete/<int:id>', views.Delete, name='Delete'),
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