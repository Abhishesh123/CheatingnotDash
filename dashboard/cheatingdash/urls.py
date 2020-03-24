from django.urls import path
from cheatingdash import views
app_name = "cheatingdash"

urlpatterns = [
    path('', views.index),
   
    
]
