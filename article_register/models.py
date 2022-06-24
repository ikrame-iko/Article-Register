from typing_extensions import Self
from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    entrees = models.IntegerField(default=0)
    sorties = models.IntegerField(default=0)

