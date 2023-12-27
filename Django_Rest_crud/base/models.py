from django.db import models

# Create your models here.

# class Item(models.Model):
#     name = models.CharField(max_length=200) ,
#     created = models.DateTimeField(auto_now_add=True)

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    # Other fields and methods of the model
