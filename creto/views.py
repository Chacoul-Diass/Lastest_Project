from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

import datetime
from creto import models


# Create your views here.

def index(request):
    return render(request, 'pages/index.html')


def gallery(request):
    data = {
        'gallery': models.PhotoGallery.objects.filter(status=True),
    }
    return render(request, 'pages/gallery.html', data)


#
# def contacts(request):
#     return render(request, 'pages/contacts.html')


def contacts(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        nom = request.POST.get('nom')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(nom, phone, email, message)
        c = models.Contact(
            nom=nom,
            phone=phone,
            email=email,
            message=message,

        )
        c.save()
        return redirect('contacts')
    else:
        el = models.Creto.objects.first()
        data = {
            'info': el,
        }

    return render(request, 'pages/contacts.html', data)
