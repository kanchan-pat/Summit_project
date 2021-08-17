from rest_framework.views import APIView
from api.serializers import BlogSerializer
from blog.models import Blog
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.mixins  import ListModelMixin, CreateModelMixin
from rest_framework.generics import ListCreateAPIView


# function, Class and GENERIC class examples of APIs

@api_view(['GET', 'POST'])
def apibloglist(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data, status=status.HTTP_200_OK)
    else:
        pass

class APIBlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    #model = Blog
    serializer_class = BlogSerializer
    #format = None


# class APIBlogList(ListModelMixin, CreateModelMixin, APIView):
#     def get(self, request):
#         blogs = Blog.objects.all()
#         return Response(BlogSerializer(blogs, many=True).data, status=status.HTTP_200_OK)

#     def post(self, request):
#         blogs_data = request.data # json => table records
#         blogs = BlogSerializer(blogs_data)  # Desiarilized data
#         if blogs.is_valid():
#             blogs.save()
#             return Response(blogs.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(blogs.data, status=status.HTTP_400_BAD_REQUEST) 

#-------------------------------------------------------------