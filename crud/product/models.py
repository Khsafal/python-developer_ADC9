from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=10)
    product_price = models.CharField(max_length=10)

    def __str__(self):
        return self.product_name
        