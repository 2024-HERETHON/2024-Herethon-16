from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def comming_soon(request):
    return render(request, 'comming_soon.html')

def index(request):
    # return render(request, 'accounts/index.html')
    return render(request, 'index.html')

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        # return redirect('accounts:login')
        return redirect('comming_soon')
    else:
        return render(request, 'signup.html', {'form' : form})

def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html', {'form' : AuthenticationForm})

    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('comming_soon')
    return render(request, 'login.html', {'form' : form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')

def mypage(request):
    return render(request, 'mypage.html')

def mypage_image_update(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)

    if request.method == "POST":
        mypage_image = request.FILES.get('mypage_image')
        if mypage_image:
            user.mypage_image.delete()
            user.mypage_image = mypage_image       
        user.save()
        return redirect('mypage')
    return render(request, 'mypage.html', {'user' : user})

def myportfolio(request):
    return render(request, 'myportfolio.html')

def mylove(request):
    return render(request, 'mylove.html')

def myviewhistory(request):
    return render(request, 'myviewhistory.html')

def mypurchase(request):
    return render(request, 'mypurchase.html')
    