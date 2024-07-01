from django.urls import path
from .views import *

#app_name = 'accounts'

urlpatterns = [
    path('',index, name = "index"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('mypage/', mypage, name="mypage"),
    path('mypage_image_update/<int:id>/', mypage_image_update, name="mypage_image_update"),
    path('myportfolio/', myportfolio, name="myportfolio"),
    path('mylove/', mylove, name="mylove"),
    path('myviewhistory/', myviewhistory, name="myviewhistory"),
    path('mypurchase/', mypurchase, name="mypurchase"),
    path('comming_soon/', comming_soon, name="comming_soon")
]