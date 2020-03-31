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
    path('contact', views.ContactMe, name='ContactMe'),
    # path('details', views.Details, name='Details'),
]