from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from portfolios.models import *
from django.db.models import Q
import random
from django.contrib.auth.decorators import login_required

@login_required
def video_list(request):
    videos = Video.objects.all()
    random_videos = random.sample(list(videos), 10)
    ranking_videos = Video.objects.order_by('-views')[:10]
    new_videos = Video.objects.order_by('-created_at')[:10]
    return render(request, "videos/video_list.html", {'videos' : videos, 'random_videos':random_videos, 'ranking_videos':ranking_videos, 'new_videos': new_videos})

@login_required
def video_detail(request, id):
    video = get_object_or_404(Video, id = id)

    views = Video.objects.get(pk=id)
    views.increase_views()
    
    if request.method == 'GET':
        WatchHistory.objects.create(
            user=request.user,
            video=video,
        )
    
    return render(request, "videos/video_detail.html",{'video' : video, 'views' : views})

@login_required
def like(request, id):
    video = get_object_or_404(Video, id = id)
    if video.like.filter(id = request.user.id).exists():
        video.like.remove(request.user)
    else:
        video.like.add(request.user)
    return redirect('videos:video_detail', id)

@login_required
def search(request):
    entered_text = request.GET['data']
    portfolios = Portfolio.objects.filter(Q(name__contains = entered_text) | Q(careers__career_title__contains=entered_text))

    videos = Video.objects.filter(Q(title__contains = entered_text) | Q(cast__contains = entered_text) | Q(staff__contains = entered_text) | Q(keyword__contains = entered_text) | Q(synopsis__contains = entered_text) | Q(staff__contains = entered_text))

    return render(request, "videos/search.html", {'portfolios': portfolios,'videos': videos, 'entered_text': entered_text})