from app_post import views
from django.urls import path

app_name = "app_post"

urlpatterns = [
    path('',views.home, name="home"),
    
]