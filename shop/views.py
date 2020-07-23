from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages

from .models import ShopCart, FavoriteProduct
from .forms import ShopCartForm
from . import models
from shop.models import Category, Product
from creto.models import Creto

# Create your views here.

# lien → {% url 'shop:home' %}
def shop(request):

    info= Creto.objects.get(pk=1)
    latestProds= models.Product.objects.reverse()[:5]
    data = {'info':info, 'latestProds':latestProds}
    return render(request, 'pages/shop/shop.html', data)

	# data = {}
    
	# tous les departements
	# 'departements':models.Departement.objects.all(),

    

def single(request, id):
    return render(request, 'pages/shop/single-shop.html')




@login_required(login_url='/login') 
def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user  # Accède auxs sessions de user

    checkoutproduit = ShopCart.objects.filter(produit_id=id)  # Verifie si ShopCart(panier) contient des produits
    if checkoutproduit:  # Condition de verification si le panier est vide
        control = 1  # Le paner contient des produits
    else:
        control = 0  # il ny a pas de produit dans le panier

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:  # On modifie notre ShopCart (si vraiment y a un produit)
                data = ShopCart.objects.get(produit_id=id)  # on initialise "data"
                data.quantity += form.cleaned_data['quantity']  # On ajout le produit
                data.save()  # enregistrer le produit dans shopcart
            else:  # le produit n'exist pas dans le panier, donc on ajoute le produit
                data = ShopCart()  # On inilialise le ShopCart
                data.user_id = current_user.id
                data.produit_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, 'Votre produit a été ajouté avec succès !!')
        return HttpResponseRedirect(url)

    else:  # s il n y a pas de post
        if control == 1:
            data = ShopCart.objects.get(produit_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.produit_id = id
            data.quantity = 1
            data.save()
        messages.success(request, 'Votre article  a été ajouté avec success !!')
        return HttpResponseRedirect(url)


@login_required(login_url='/login') 
def favorite(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user  # Accède auxs sessions de user

    checkoutproduit = FavoriteProduct.objects.filter(produit_id=id)  # Verifie si ShopCart(panier) contient des produits
    if checkoutproduit:  # Condition de verification si le panier est vide
        control = 1  # Le paner contient des produits
    else:
        control = 0  # il ny a pas de produit dans le panier

    if control == 0:
        data = ShopCart()
        data.user_id = current_user.id
        data.produit_id = id
        data.quantity = 1
        data.save()
        messages.success(request, 'Votre article  a été ajouté avec success !!')
        return HttpResponseRedirect(url)

    else:
        messages.success(request, 'Ce produit est deja dans votre favorie')
        return HttpResponseRedirect(url)
            
        
       
            

            
        

    
