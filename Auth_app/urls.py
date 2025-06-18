from django.urls import path
from . import views

app_name = 'auth_app'

urlpatterns = [
    path('sign-up/',views.sign_up, name='signup'),
    path('login/', views.Log_in, name="login"),
]