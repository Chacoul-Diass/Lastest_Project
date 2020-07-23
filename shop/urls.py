from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path('shop', views.shop, name='shop'),

	# path('single-product/<int:id>/', views.single_product, name="single-product"),

]