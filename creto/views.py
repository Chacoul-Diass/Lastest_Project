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

        data = {'produit': produit, 'prod': prod, 'categories': categories}
        return render(request, 'pages/index.html', data)



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

        return render(request, 'pages/contacts.html')

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


