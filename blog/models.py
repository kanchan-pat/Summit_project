from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class AppUser(models.Model):
    pass


class Blog(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.CharField(max_length=2000)
    create_date = models.DateField()
    publication_date = models.DateField()
    author = models.ForeignKey(AppUser, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.title