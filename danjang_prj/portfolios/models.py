from django.db import models
from accounts.models import User
import os
from uuid import uuid4
from django.utils import timezone

# 파일 경로 중복 예방
def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'


class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

"""
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
"""

class Portfolio(models.Model):
    user = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name='portfolios', null=True)
    name = models.CharField(max_length=10) # 이름
    role = models.ManyToManyField(to=Role, through="PortfolioRole", related_name="portfolios") # 전문분야
    profile_photo = models.ImageField(verbose_name="프로필사진", blank=True, upload_to=upload_filepath) # 프로필 사진
    email = models.EmailField(max_length=128, verbose_name="이메일", blank=True)
    one_line = models.CharField(verbose_name="한줄소개", max_length=128, blank=True) # 한 줄 소개
    intro = models.TextField(verbose_name="소개글", blank=True) # 소개글
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True) # 포폴 만든 시간 > 포폴 시간 순 배열에 쓰기
    
    def __str__(self):
        return self.name
    
class PortfolioRole(models.Model):
    role = models.ForeignKey(to = Role, on_delete=models.PROTECT, related_name="roles_portfoliorole")
    portfolio = models.ForeignKey(to = Portfolio, on_delete=models.CASCADE, related_name="portfolios_portfoliorole")

class Career(models.Model): # 경력
    career_title = models.CharField(verbose_name="작품명", max_length=128)   
    career_role = models.CharField(verbose_name="역할", max_length=128)
    career_year = models.IntegerField(verbose_name="연도", default=2024, null=True)
    portfolio = models.ForeignKey(to = Portfolio, on_delete=models.CASCADE, related_name="careers")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="careers")

class Video(models.Model): # 포트폴리오 video
    user = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(verbose_name="제목", max_length=200, blank=True)
    cast = models.CharField(verbose_name="출연진", max_length=128, blank=True) 
    staff = models.CharField(verbose_name="스탭", blank=True, max_length=128) 
    price = models.IntegerField(verbose_name="가격", default=1000, blank=True)
    keyword = models.TextField(verbose_name="키워드", blank=True)
    synopsis = models.TextField(verbose_name="시놉시스", blank=True)
    video = models.FileField(verbose_name="동영상", upload_to=upload_filepath, blank=True)
    myurl = models.URLField(blank=True, null=True)
    portfolio = models.ForeignKey(to = Portfolio, on_delete=models.CASCADE, related_name="videos")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(verbose_name="이미지", blank=True, null=True, upload_to=upload_filepath)
    portfolio = models.ForeignKey(to=Portfolio, on_delete=models.CASCADE, related_name='photos')