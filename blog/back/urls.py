from django.conf.urls import url

from back import views

urlpatterns = [
    url(r'^register/', views.register),
    url(r'^login/', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^article/', views.article, name='article'),
    url(r'^add_art/', views.add_art, name='add_art'),
]