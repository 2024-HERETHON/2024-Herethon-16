from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # 회원가입/로그인 기능
    path('',index, name = "index"),
    path('signup/', signup_view, name="signup"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    # 마이페이지
    path('mypage/', mypage, name="mypage"),
    path('mypage_image_update/<int:id>/', mypage_image_update, name="mypage_image_update"),
    path('create_myportfolio/', create_myportfolio, name="create_myportfolio"),
    path('update_myportfolio/', update_myportfolio, name="update_myportfolio"),
    #path('create_my_career/<int:portfolio_id>/', create_my_career, name='create_my_career'),
    path('mylove/', mylove, name="mylove"),
    path('myviewhistory/', myviewhistory, name="myviewhistory"),
    path('mypurchase/', mypurchase, name="mypurchase"),
    path('comming_soon/', comming_soon, name="comming_soon")
]