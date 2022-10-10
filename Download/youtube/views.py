from django.shortcuts import render
from pytube import YouTube
import os

def youtube_home(request):
    return render(request, "home.html")

def download(request):
    global url
    url = request.GET.get('url')
    yt = YouTube(url)
    video = []
    video = yt.streams.filter(progressive = True, file_extension="mp4").all()
    embed_link = url.replace("watch?v=", "embed/")
    Title = yt.title
    return render(request, "download.html", {'video': video, 'embed': embed_link, 'title':Title})

def yt_download_done(request,resolution):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == "POST":
        YouTube(url).streams.get_by_resolution(resolution).download(dirs)
        return render(request, 'done.html')
    else:
        return render(request, 'error.html')
    
   