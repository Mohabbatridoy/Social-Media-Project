from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('sign-up/',views.sign_up, name='signup'),
    path('login/', views.Log_in, name="login"),
    path('edit-profile/', views.Edit_Profile, name='edit_profile'),
    path('logout/', views.LogOut, name="logout"),
    path('profile/', views.Profile, name="profile"), 
    path('user-other/<username>',views.user, name="user_other"),
    path('follow/<username>', views.follow, name="follow"),
    path('unfollow/<username>', views.unfollow, name="unfollow")
]