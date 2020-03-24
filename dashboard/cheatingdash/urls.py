from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index),
    path('userlist', views.userList, name='userList'),
    path('login', views.Login),
    path('logout', views.Logout, name='Logout'),
    path('delete/<int:id>', views.Delete, name='Delete'),
    # path('details', views.Details, name='Details'),
]