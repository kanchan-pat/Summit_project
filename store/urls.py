from django.contrib import admin
from django.urls import path, re_path
from store.views import Category


app_name ='store'
urlpatterns = [
    # #path('', list_blogs, name='list_blogs'),   # with function 
    path('', Category.as_view(), name='list_category'),  # with class

    # #path('<int:blog_id>/', blog_details, name='blog_details'),  # with function 
    # path('<int:pk>/', BlogDetail.as_view(), name='blog_details'),  # with class

    # # create
    # #path('create/', blog_create, name='blog_create'),          # with function 
    # path('classbasecreate/', BlogCreate.as_view(), name='blog_create'),   # class from View
    # path('create/', BlogCreateGeneric.as_view(), name='blog_create'),         # with updated Class

    # # update
    # #path('<int:blog_id>/update/', blog_update, name='blog_update'),
    # #re_path(r'^(?P<blog_id>\d+)/update/$', blog_update, name='blog_update'),  
    # re_path(r'^(?P<pk>\d+)/update/$', BlogUpdateGeneric.as_view(), name='blog_update')    # option with Class Generic
]
