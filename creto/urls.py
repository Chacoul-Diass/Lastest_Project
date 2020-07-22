from django.urls import path
from creto import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('contacts', views.contacts, name='contacts'),
]
