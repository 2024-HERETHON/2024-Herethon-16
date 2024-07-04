from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *

# 포트폴리오 보기
def portfolio_list(request):
    #portfolios = Portfolio.objects.all().order_by('-created_at').prefetch_related('careers', 'videos', 'photos')
    selected_roles = request.GET.getlist('roles')
    if selected_roles:
        portfolios = Portfolio.objects.filter(role__in=selected_roles).distinct().order_by('-created_at').prefetch_related('careers', 'videos', 'photos')
    else:
        portfolios = Portfolio.objects.all().order_by('-created_at').prefetch_related('careers', 'videos', 'photos')
    roles = Role.objects.all()
    
    return render(request,"portfolios/portfolio_list.html", {"portfolios" : portfolios, 'roles': roles, 'selected_roles': selected_roles})

# 상세 포트폴리오
def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id = id)
    return render(request, "portfolios/portfolio_detail.html", {"portfolio":portfolio})
