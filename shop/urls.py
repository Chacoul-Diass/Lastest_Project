from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path('shop', views.shop, name='shop'),
<<<<<<< HEAD

	# path('single-product/<int:id>/', views.single_product, name="single-product"),

    #AddtoCart
    path('addtocart/<int:id>', views.add_to_cart, name='addtocart'),


=======
    path('single/<int:id>/', views.single, name='single'),
	
>>>>>>> 926dd522385aab4aa95472efb3683e8fa543b7eb
]