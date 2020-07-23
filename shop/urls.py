from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path('shop', views.shop, name='shop'),

    # AddtoCart
    path('addtocart/<int:id>', views.add_to_cart, name='addtocart'),

    path('single/<int:id>', views.single, name='single'),
	
]