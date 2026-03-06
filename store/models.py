from djongo import models
from django.db import models
  
class Product(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=50)
    tags = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.namepythp