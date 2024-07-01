from django.db import models
from accounts.models import User

role_select = ( # 전문분야
    ('감독', '감독'),
    ('배우', '배우'),
    ('성우', '성우'),
    ('연출', '연출'),
    ('음향', '음향'),
    ('조명', '조명'),
    ('의상', '의상'),
    ('메이크업', '메이크업'),
    ('아역', '아역'),
    ('모델', '모델'),
    ('인플루언서', '인플루언서')
)


class Portfolio(models.Model):
    name = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name='portfolios') # 이름
    role = models.CharField(max_length=20, choices=role_select) # 전문분야
    profile_photo = models.ImageField(verbose_name="프로필사진", blank=True, upload_to='profile_photo') # 프로필 사진
    email = models.EmailField(max_length=128, verbose_name="이메일", blank=True)
    one_line = models.CharField(verbose_name="한줄소개", max_length=128, blank=True) # 한 줄 소개
    intro = models.TextField(verbose_name="소개글", blank=True) # 소개글

    def __str__(self):
        return self.name
    