from django.urls import path
from .views import *

app_name = 'portfolios'

urlpatterns = [
    # 포트폴리오
    path('portfolio_list/', portfolio_list, name="portfolio_list"),
    path('portfolio_detail/<int:id>/', portfolio_detail, name="portfolio_detail"),
]