from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	titre = models.CharField(max_length=255)
	status = models.BooleanField(default=True)

	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Categorie"
		verbose_name_plural = "Les Categories"

	def __str__(self):
		return self.titre


class Product(models.Model):
	titre = models.CharField(max_length=255)
	detais = models.CharField(max_length=255)
	image0 = models.ImageField(upload_to = 'shop/produit/image', blank=True, null =True)
	image1 = models.ImageField(upload_to = 'shop/produit/image', blank=True, null =True)
	image2 = models.ImageField(upload_to = 'shop/produit/image', blank=True, null =True)
	image3 = models.ImageField(upload_to = 'shop/produit/image', blank=True, null =True)
	prix = models.FloatField()
	reduction = models.FloatField(blank=True)
	categorie = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'categorie')
	status = models.BooleanField(default=True)
	recommande = models.BooleanField(default=False)
	description = models.TextField(default='Aucune description')


	date_cre = models.DateTimeField(auto_now_add=True)
	date_mod = models.DateTimeField(auto_now=True) 

	class Meta:
		verbose_name = "product"
		verbose_name_plural = "Les Products"

	def __str__(self):
		return self.titre
	

class ShopCart(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	produit = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField()