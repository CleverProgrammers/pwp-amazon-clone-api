from django.db import models
from users.models import User

# Create your models here.
class Address(models.Model):
    address_type = models.CharField(max_length=255, null=True)
    house_num = models.CharField(max_length=255, null=False)
    street = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    zip_code = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=None)
