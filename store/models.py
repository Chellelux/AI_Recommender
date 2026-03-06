from django.db import models
from djongo import models as djongo_models

class Product(models.Model):
    _id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name