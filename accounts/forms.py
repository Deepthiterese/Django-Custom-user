# accounts/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
