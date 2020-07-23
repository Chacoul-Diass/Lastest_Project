from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import datetime
from . import models
from shop.models import Category, Product

# Create your views here.

# lien → {% url 'shop:home' %}
def shop(request):

	data = {
	# tous les departements
	# 'departements':models.Departement.objects.all(),

	# les 5 derniers produits en ordre decroissant de id
	# 'latestProds':models.Product.objects.reverse()[:5],

	# 'recomProds':models.Product.objects.filter(recommande=True).reverse()[:10],

	'nbArticles':Product.objects.count(),

	'products' : Product.objects.all(),

	# 'info':Info.objects.first(),
	}

	return render(request, 'pages/shop/shop.html',data)


def single(request):
    return render(request, 'pages/shop/single-shop.html')
