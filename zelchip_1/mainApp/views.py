from django.shortcuts import render


# Create your views here.

def index(request):
    string = 'Hello, world'
    context = {'string': string}
    return render(request, 'mainApp/index.html', context)

def detail(request):
    string = 'My name is Bond ' \
             'James Bond'
    context = {'string': string}
    return render(request, 'mainApp/detail.html', context)