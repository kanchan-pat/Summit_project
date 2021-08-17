from django.contrib import admin
from django.urls import path, re_path
from store.views import Category, CategoryUpdate, CategoryDetail, CategoryCreate, Product


app_name ='store'
urlpatterns = [
    path('', Category.as_view(), name='list_category'),  
    path('<int:pk>/', CategoryDetail.as_view(), name='category_details'),  
    path('create/', CategoryCreate.as_view(), name='category_create'),         
    re_path(r'^(?P<pk>\d+)/update/$', CategoryUpdate.as_view(), name='category_update'),

    #re_path('<str:category_name>/',)
    path('products/', Product.as_view(), name='list_products'), 
]
