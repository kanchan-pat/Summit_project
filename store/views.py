from django.shortcuts import render
from django.views.generic.list import ListView
from store.models import Categories
# Create your views here.



class Category(ListView): 
    model = Categories
    template_name = 'store/main.html'
    context_object_name = 'Category_key'

# Add more views for CRUD 
