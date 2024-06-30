from django.urls import path
from .views import *

# app_name = 'accounts'

urlpatterns = [
    path('',index, name = "index"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('mypage/', mypage, name="mypage"),
    path('comming_soon', comming_soon, name="comming_soon")
]