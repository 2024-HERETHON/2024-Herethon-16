from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from portfolios.models import *

def comming_soon(request):
    return render(request, 'accounts/comming_soon.html')

def index(request):
    return render(request, 'accounts/index.html')

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form' : form})

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('accounts:comming_soon')
    else:
        return render(request, 'accounts/signup.html', {'form' : form})

def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm})

    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('accounts:comming_soon')
    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('accounts:index')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def mypage_image_update(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)

    if request.method == "POST":
        mypage_image = request.FILES.get('mypage_image')
        if mypage_image:
            user.mypage_image.delete()
            user.mypage_image = mypage_image       
        user.save()
        return redirect('accounts:mypage')
    return render(request, 'accounts/mypage.html', {'user' : user})

def create_myportfolio(request):
    roles = Role.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        profile_photo = request.FILES.get('profile_photo')
        email = request.POST.get('email')
        one_line = request.POST.get('one_line')
        intro = request.POST.get('intro')

        role_ids = request.POST.getlist('role')
        role_list = [get_object_or_404(Role, id = role_id) for role_id in role_ids]

        portfolios = Portfolio.objects.create(
            name = name,
            profile_photo = profile_photo,
            email = email,
            one_line = one_line,
            intro = intro,
            user = request.user,
        )

        for role in role_list:
            portfolios.role.add(role)

        return redirect('accounts:mypage')
    return render(request, 'accounts/create_myportfolio.html', {'roles' : roles})
""" 경력사항 보류
def create_my_career(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, id=portfolio_id)
    if request.method == "POST":
        Career.objects.create(
            career_title = request.POST.get('career_title'),
            career_role = request.POST.get('career_role'),
            career_year = request.POST.get('career-year'),
            portfolio = portfolio,
            author = request.user,
        )
        return redirect('accounts:create_myportfolio', portfolio_id)
"""
def update_myportfolio(request):
    if request.method == "GET":
        myportfolio = Portfolio.objects.get(user=request.user)
        roles = Role.objects.all()
        return render(request, 'accounts/update_myportfolio.html', {'myportfolio': myportfolio, 'roles': roles})
    elif request.method == "POST":
        myportfolio = Portfolio.objects.get(user=request.user)
        myportfolio.name = request.POST.get('name')
        #전문 분야
        role_ids = request.POST.getlist('role')
        role_list = [get_object_or_404(Role, id=role_id) for role_id in role_ids]
        myportfolio.role.set(role_list)

        #이미지
        myportfolio.email = request.POST.get('email')
        myportfolio.one_line = request.POST.get('one_line')
        myportfolio.intro = request.POST.get('intro')



        myportfolio.save()
        return redirect('accounts:update_myportfolio')
    

def mylove(request):
    return render(request, 'accounts/mylove.html')

def myviewhistory(request):
    return render(request, 'accounts/myviewhistory.html')

def mypurchase(request):
    return render(request, 'accounts/mypurchase.html')
    