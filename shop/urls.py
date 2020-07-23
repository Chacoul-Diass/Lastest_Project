from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path('shop', views.shop, name='shop'),

    # path('single-product/<int:id>/', views.single_product, name="single-product"),

    # AddtoCart
    path('addtocart/<int:id>', views.add_to_cart, name='addtocart'),

<<<<<<< HEAD

    path('single', views.single, name='single'),
	
]
=======
    path('single/<int:id>/', views.single, name='single'),
]
>>>>>>> 6ccbb720ed14a79d7426065062798992a76354da
