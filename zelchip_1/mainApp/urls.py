from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('photos/', views.get_photos, name='photos'),
    path('news/', views.get_news, name='news'),
]
