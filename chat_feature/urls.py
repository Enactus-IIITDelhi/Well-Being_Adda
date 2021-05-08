from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
app_name = 'chat_feature'

urlpatterns = [
    path("home/", views.index, name="home"),
    path('chat/', views.chat_index, name='chat_index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('account/register/', views.register, name='register'),
    path('account/profile', views.profile, name='profile'),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('posts', views.posts, name="posts"),
    path('team', views.team, name="team"),
]
