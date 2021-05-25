from django import forms
from .models import Product

class ListForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    target = forms.CharField(label='Search Target')
