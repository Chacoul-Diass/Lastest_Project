from django.urls import path
from creto import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gallery', views.gallery, name='gallery'),
    path('contacts', views.contacts, name='contacts'),

    #lien inscription
    path('sign-up', views.signup_form, name='sign-up'),
    #connexion
    path('log-in', views.log_in, name='log-in'),
    #deconnexion
    path('log-out', views.log_out, name='log-out'),

]
