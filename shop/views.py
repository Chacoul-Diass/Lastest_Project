from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import datetime
from django.contrib import messages

from .models import ShopCart
from .forms import ShopCartForm
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from . import models
from shop.models import Category, Product

# Create your views here.

# lien → {% url 'shop:home' %}
def shop(request):
    return render(request, 'pages/shop/shop.html')

	# data = {}
    
	# tous les departements
	# 'departements':models.Departement.objects.all(),

	# les 5 derniers produits en ordre decroissant de id
	# 'latestProds':models.Product.objects.reverse()[:5],

	# 'recomProds':models.Product.objects.filter(recommande=True).reverse()[:10],

def single(request):
    return render(request, 'pages/shop/single-shop')


def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user #Accède auxs essions de user

    checkoutproduit = ShopCart.objects.filter(produit_id=id) #Verifie si ShopCart(panier) contient des produits
    if checkoutproduit: #Condition de verification si le panier est vide
        control = 1 # Le paner contient des produits
    else:
        control = 0 #il ny a pas de produit dans le panier

    if request.method=='POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control ==1: #On modifie notre ShopCart (si vraiment y a un produit)
                data = ShopCart.objects.get(produit_id=id) #on initialise "data"
                data.quantity += form.cleaned_data['quantity'] #On ajout le produit 
                data.save() #enregistrer le produit dans shopcart
            else: #le produit n'exist pas dans le panier, donc on ajoute le produit
                data = ShopCart() #On inilialise le ShopCart
                data.user_id = current_user.id
                data.produit_id =id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Votre produit a été ajouté avec succès !!')
        return HttpResponseRedirect(url)

    else: # s il n y a pas de post
        if control == 1:
            data = ShopCart.objects.get(produit_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.produit_id=id
            data.quantity = 1
            data.save()
        messages.success(request, 'Votre article  a été ajouté avec success !!')
        return HttpResponseRedirect(url)

    
