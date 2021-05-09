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
    path('events', views.events, name="events"),
    path('posts', views.posts, name="posts"),
    path('team', views.team, name="team"),
    path('contactus', views.contactus, name="contactus"),
    path('blogs', views.blogs, name="blogs"),
    path('expKheya', views.expKheya, name="expKheya"),
    path('expOjasvi', views.expOjasvi, name="expOjasvi"),
    path('newsLY', views.newsLY, name="newsLY"),
    path('newsWellBeing', views.newsWellBeing, name="newsWellBeing"),
    path('eventArtTherapy', views.eventArtTherapy, name="eventArtTherapy"),
    path('eventMentalMyths', views.eventMentalMyths, name="eventMentalMyths"),
    path('eventMentalStigma', views.eventMentalStigma, name="eventMentalStigma"),
    path('eventSelfHub', views.eventSelfHub, name="eventSelfHub"),
    path('eventSuicidePrevention', views.eventSuicidePrevention, name="eventSuicidePrevention"),
    path('eventThankful', views.eventThankful, name="eventThankful"),
    path('eventChildhood', views.eventChildhood, name="eventChildhood"),
    path('eventSofia', views.eventSofia, name="eventSofia"),
]
