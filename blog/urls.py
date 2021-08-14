from django.contrib import admin
from django.urls import path
from blog.views import list_blogs, blog_details



urlpatterns = [
    path('', list_blogs, name='list_blogs'),
    path('<int:pk>/', blog_details)
]
