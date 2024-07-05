from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *
from django.contrib.auth.decorators import login_required

# 포트폴리오 보기
@login_required
def video_list(request):
    videos = list(Video.objects.all())
    if len(videos) < 10:
        random_videos = videos
        ranking_videos = sorted(videos, key=lambda x: x.views, reverse=True)[:10]
        new_videos = sorted(videos, key=lambda x: x.created_at, reverse=True)[:10]
    else:
        random_videos = random.sample(videos, 10)
        ranking_videos = sorted(videos, key=lambda x: x.views, reverse=True)[:10]
        new_videos = sorted(videos, key=lambda x: x.created_at, reverse=True)[:10]
    return render(request, "videos/video_list.html", {'videos': videos, 'random_videos': random_videos, 'ranking_videos': ranking_videos, 'new_videos': new_videos})

# 상세 포트폴리오
@login_required
def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id = id)
    return render(request, "portfolios/portfolio_detail.html", {"portfolio":portfolio})
