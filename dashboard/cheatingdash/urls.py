from django.urls import path
from cheatingdash import views
app_name = "cheatingdash"

from . import views


urlpatterns = [
    path('', views.Index),
    path('login', views.Login),
    path('login', views.Logout, name='Logout'),
    path('paymentStatus/',views.paymentStatus,name='paymentStatus')
]
