from django.urls import path
from .views import *
from videos import views

app_name = 'videos'

urlpatterns = [
    path("", video_list, name="video_list"),
    path("video_detail/<int:id>/", video_detail, name="video_detail"),
    path("<int:id>/like/", like, name="like"),
    path("search/", search, name="search"),
]