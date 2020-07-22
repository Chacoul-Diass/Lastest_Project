from django.shortcuts import render
import datetime
from creto import models


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def gallery(request):
    return render(request, 'pages/gallery.html')


def contacts(request):
    return render(request, 'pages/contacts.html')