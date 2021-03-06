from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
app_name = 'chat_feature'

urlpatterns = [
    path("home/", views.index, name="home"),
    path('chat/', views.chat_index, name='chat_index'),
    path("chat_test",views.chat,name='chat_test'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('account/register/', views.register, name='register'),
    path('account/profile', views.profile, name='profile'),
    path('about', views.about, name="about"),
    path('chat_bot', views.chat_bot, name='chat_bot')
]
