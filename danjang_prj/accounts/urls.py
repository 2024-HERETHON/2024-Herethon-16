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
    path('create_my_career/', create_my_career, name='create_my_career'),
    path('delete_my_career/<int:id>/', delete_my_career, name="delete_my_career"),

    # 사진 및 영상 업로드
    path('create_my_video/', create_my_video, name="create_my_video"),
    path('delete_my_video/<int:id>/', delete_my_video, name="delete_my_video"),
    path('delete_my_photo/<int:id>/', delete_my_photo, name="delete_my_photo"),
    path('mylike/', mylike, name="mylike"),
    # path('my_like/<int:video_id>/',mylike, name="mylike"),
    path('myviewhistory/', myviewhistory, name="myviewhistory"),
    path('comming_soon/', comming_soon, name="comming_soon")
]