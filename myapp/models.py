from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    