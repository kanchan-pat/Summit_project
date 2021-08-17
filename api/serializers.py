from rest_framework.serializers import ModelSerializer
from blog.models import Blog


class BlogSerializer(ModelSerializer):  # convert to Json type of data
    class Meta:
        model = Blog
        fields = '__all__'
