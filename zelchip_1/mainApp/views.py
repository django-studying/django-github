import random

from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    string = 'Hello, world'
    last_new = News.objects.order_by('-pub_date')[:1][0]
    photo = random.choice(Photos.objects.all())
    context = {'string': string, 'last_new': last_new, 'photo': photo}
    return render(request, 'mainApp/index.html', context)


def detail(request):
    string = 'My name is Bond ' \
             'James Bond'
    context = {'string': string}
    return render(request, 'mainApp/detail.html', context)


def get_news(request):
    news = News.objects.order_by('-pub_date')
    context = {'news': news}
    return render(request, 'mainApp/news.html', context)


def get_photos(request):
    photo = Photos.objects.all()
