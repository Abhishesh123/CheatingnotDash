from django.urls import path
from . import views
app_name = "cheatingnotfront"
urlpatterns = [
    path('', views.Index),
    path('Login/', views.Login.as_view(),name="Login"), 
    path('VerifyOTP/',views.VerifyOTP.as_view(),name="VerifyOTP")
    


]