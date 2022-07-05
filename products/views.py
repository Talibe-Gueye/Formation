from django.shortcuts import render
from django.http import HttpResponse


def home(request, *args, **kwargs):
    myList = [3,44,5,32,66]
    return render(request, 'index.html', {'list':myList})

def contact(request):
    return HttpResponse("Contact me")

def blog(request):
    return HttpResponse("Blog page")

def accueil(request):
    return HttpResponse('<h1>Accueil</h1>')
