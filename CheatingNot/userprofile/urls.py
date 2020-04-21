from django.urls import path
from userprofile import views 


urlpatterns = [
    path('', views.index, name='home'),  # home page
    path('register_login', views.RegisterOLogin.as_view()),      # user auth page
    path('verify_otp', views.VerifyOTP.as_view()),      # user auth page
    path('resend_otp', views.ResendOTP.as_view()),      # user auth page 
    path('create_user', views.CreateUser.as_view()),  # create user page
    
    
    path('add_photo', views.AddPhoto.as_view()),  # add profile pic
    path('delete_photo', views.DeletePhoto.as_view()),  # add profile pic              
    path('add_video', views.AddVideo.as_view()),  # add more Vedios
    path('delete_video', views.DeleteVedio.as_view()),  # add more Vedios
    path('user_preferences', views.UserPreferences.as_view()),  # add more Vedios
    
    path('userlisting', views.UserListing.as_view()),  # add more Vedios
    path('dropdown_list', views.DropDownList.as_view()),  # add more Vedios
    
    path('user_info', views.UserInfo.as_view()),  # create user page  
    
    
    path('user_search', views.UserSearch.as_view()),  # User Search by name
    path('user_notifications', views.Notification.as_view()),  # User Search by name
    path('notification_users_details', views.NotificationsUsersDetails.as_view()),  # User Search by name
    path('like', views.UserLikes.as_view()),  
    path('superlike', views.UserSuperLikes.as_view()),  
    path('heart', views.UserHearts.as_view()),  
    path('hi', views.UserHi.as_view()),  
    path('nope', views.UserNopes.as_view()),  
    path('suspend_user', views.SuspendUser.as_view()),
    path('my_likes', views.MyLikes.as_view()),
    
    
    
      # create user page
    
    
    # User Actions
#     path('mylikes/<user_id>', views.MyLikes.as_view()),  # User Search by name


    

    ]