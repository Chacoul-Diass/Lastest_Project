from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

import datetime
from creto import models


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def gallery(request):
    return render(request, 'pages/gallery.html')

#
# def contacts(request):
#     return render(request, 'pages/contacts.html')


def contacts(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':

        nom = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('comments')

        c = models.Contact(
            nom=nom,
            phone=phone,
            email=email,
            message=message,

        )
        c.save()
        return redirect('creto:index')
    else:
        data = {
            'contacts': models.Contact.objects.filter(status=True),

        }
        return render(request, 'pages/contacts.html')