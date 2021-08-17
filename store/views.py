from django.shortcuts import render
from django.views import generic
from store.models import Categories, Products
from store.forms import CategoryForm
from django.urls.base import reverse_lazy
# Create your views here.



class Category(generic.ListView):
    model = Categories
    template_name = 'store/main.html'
    context_object_name = 'category_key'


class CategoryUpdate(generic.UpdateView):
    model = Categories
    template_name = 'store/category_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')
    

class CategoryDetail(generic.DetailView):
    model = Categories
    template_name = 'store/category_detail.html'


class CategoryCreate(generic.CreateView):
    model = Categories
    template_name = 'store/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('store:list_category')




class Product(generic.ListView):
    model = Products
    # Here we are not sending the extra context 'category_key' to the template and that's the reason why it's not displaying any categories.
    # so Either a) send this extra context data 
    # or b) send Categories only and use the Foreign key relation between Category and Products and get the related products in template 
    template_name = 'store/all_products.html' 
    context_object_name = 'products_key'
