from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50, label='username')
    email = forms.EmailField(max_length=100, label='Email adr')
    first_name = forms.CharField(max_length=50, label='Firstname')
    last_name = forms.CharField(max_length=50, label='Firstname')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password2', 'password2',)

    