from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from blog.forms import BlogForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from blog.models import Blog
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView


# function and class to show List of Items
def list_blogs(request):
    blogs = Blog.objects.all()  
    return render(request, 'blog/index.html', {'blogs_key': blogs})

class BlogList(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'blogs_key'
# -------------------------------------------


# function and class to show particular item
def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # pk = primary key, in SQlite table Primary key is "id" column
    return render(request, 'blog/blog_detail.html', {'blog': blog})

class BlogDetail(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    # context_object_name = 'blog' # by default it will be "object"
# -------------------------------------------





# Example of Update with function, with class(View) and with class(UpdateView):
def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # already exist 
    form = BlogForm(request.POST or None, instance=blog)
    if request.method == 'GET':
        return render(request, 'blog/blog_update.html', {'blog_form': form})
    else: # POST 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:list_blogs'))
        else:
            return render(request, 'blog/blog_update.html', {'blog_form': form})

class BlogUpdateGeneric(UpdateView):
    model = Blog
    template_name = 'blog/blog_update.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog:list_blogs')
# -------------------------------------------   




# Example of Create with function, with class(View) and with class(CreateView):
def blog_create(request):
    if request.method == 'GET':
        form = BlogForm
        return render(request, 'blog/blog_create.html', {'blog_form': form})
    else: # POST
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:list_blogs'))
        else:
            return render(request, 'blog/blog_create.html', {'blog_form': form})

class BlogCreate(View):
    def get(self, request):
        form = BlogForm
        return render(request, 'blog/blog_create.html', {'blog_form': form})
    def post(self, request): 
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:list_blogs'))
        else:
            return render(request, 'blog/blog_create.html', {'blog_form': form})


class BlogCreateGeneric(CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    form_class = BlogForm
    #fields = ['title', 'text']
    success_url = reverse_lazy('blog:list_blogs')
# -------------------------------------------