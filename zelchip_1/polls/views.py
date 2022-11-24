from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def index(request):
   name_all = Main_barlist.objects.all()
   name_list = [name_all[i].name for i in range(len(name_all))]
   context = {'name_list': name_list}
   return render(request, 'polls/index.html', context)

def about(request):
    pass

def contacts(request):
    pass

def manufacture(request):
    pass

def search(request):
    pass

def delivery(request):
    pass

