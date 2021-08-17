from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', include('blog.urls')),
    path('store/', include('store.urls')),
    #path('api/blogs/', views.apibloglist),  # with function 
    path('api/blogs/', views.APIBlogList.as_view()),  # with class
]
