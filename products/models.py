from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(null=True, decimal_places=2, max_digits=6)
    rating = models.PositiveIntegerField(null=True)
    image = models.ImageField(null=True)
    stock = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name} - ${self.price}'
