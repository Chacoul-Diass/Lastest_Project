from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import SignupForm

import datetime
from creto import models

from shop.models import Product, Category


# Create your views here.

<<<<<<< HEAD
def index(request):
    produit = Product.objects.filter().order_by('-id')[:5]
    prod = Product.objects.filter().order_by('id')[:8]
    data = {'produit':produit, 'prod':prod}
    return render(request, 'pages/index.html', data)
=======
def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST.get('subscribe')
        print(email)
        c = models.Suscribe(
            email=email,
        )
        c.save()
        return redirect('home')
    else:
        categories = Category.objects.filter(status=True)
        produit = Product.objects.filter(status=True).order_by('date_mod')[:5]
        prod = Product.objects.filter(status=True).order_by('date_mod')[:8]
        feedback = models.Contact.objects.filter(status=True)
        data = {'produit': produit, 'prod': prod, 'categories': categories, 'feedback': feedback}
        return render(request, 'pages/index.html', data)

>>>>>>> 6ccbb720ed14a79d7426065062798992a76354da


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
<<<<<<< HEAD
=======

<<<<<<< HEAD
>>>>>>> 6ccbb720ed14a79d7426065062798992a76354da
        return render(request, 'pages/contacts.html')
=======
        return render(request, 'pages/contacts.html', data)
>>>>>>> bff25136d7e8476f8250ae4d1eff70c6d531d1e1

#inscription
def signup_form(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            #On recupère le @username et @password pour connecter l'utilisateur
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, 'votre compte a ete creer avec success')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/sign-up')
    else:
        form = SignupForm()
    return render(request, 'user/sign-up.html', {'form':form})

def log_in(request):
    if request.method=='POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, 'vous etes bien connecté')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'username or password incorrect')
            return HttpResponseRedirect('/log-in')
    return render(request, 'user/login.html')

#deconnexion
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
<<<<<<< HEAD
=======


>>>>>>> 6ccbb720ed14a79d7426065062798992a76354da
