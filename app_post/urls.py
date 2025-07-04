from app_post import views
from django.urls import path

app_name = "app_post"

urlpatterns = [
    path('',views.home, name="home"),
    path('liked/<pk>', views.Liked, name="liked"),
    path('unlike/<pk>',  views.Unliked, name="unliked"), 
    path('comment/<pk>', views.Comment, name="comment"),
]