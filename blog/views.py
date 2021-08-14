from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog


def list_blogs(request):
    list_blogs = Blog.objects.all()  
    return render(request, 'blog/index.html', {'blogs_key': list_blogs})

def blog_details():
    pass