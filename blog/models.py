from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50, null=False)
    text = models.CharField(max_length=2000)
    create_date = models.DateField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title