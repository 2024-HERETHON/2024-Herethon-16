from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from accounts.models import *
from django.contrib.auth.decorators import login_required

# 포트폴리오 보기
@login_required
def portfolio_list(request):
    roles = Role.objects.all()
    selected_role_id = request.GET.get('roles')
    if selected_role_id:
        selected_role = get_object_or_404(Role, id=selected_role_id)
        portfolios = selected_role.portfolios.all().order_by('-created_at').prefetch_related('careers', 'videos', 'photos')
        return render(request, "portfolios/portfolio_list.html", {"portfolios": portfolios, 'roles': roles, 'selected_role': selected_role})
    else:
        portfolios = Portfolio.objects.all().order_by('-created_at').prefetch_related('careers', 'videos', 'photos')
        return render(request, "portfolios/portfolio_list.html", {"portfolios": portfolios, 'roles': roles})

# 상세 포트폴리오
@login_required
def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, id = id)
    return render(request, "portfolios/portfolio_detail.html", {"portfolio":portfolio})
