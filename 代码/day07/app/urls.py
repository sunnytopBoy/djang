from django.conf.urls import url

from app import views

urlpatterns =[
    # 创建文章
    url(r'^add_art', views.add_art, name='add'),
    # 文章列表
    url(r'^art', views.art, name='art_list'),
]