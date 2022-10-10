from django.urls import path
from . import views

app_name = 'yt_downloader' 

urlpatterns = [
    path('home/', views.youtube_home, name="home"),
    path('download/', views.download, name="download"),
    path('download/<resolution>/', views.yt_download_done, name='download_done'),
]
