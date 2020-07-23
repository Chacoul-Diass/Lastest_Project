from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import datetime

# Create your views here.




# Create your views here.

def shop(request):
    return render(request, 'pages/shop/shop.html')


def single(request):
    return render(request, 'pages/shop/single-shop.html')
