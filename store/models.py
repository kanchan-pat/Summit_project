from django.db import models
from django.db.models.fields import CharField
# Create your models here.


class Categories(models.Model):
    name = CharField(max_length=50, null=False)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Products(models.Model):
    pass