from django.db import models
from favorite import models as m

class LoginUser(models.Model):
    login = models.CharField(max_length=64, blank=True, null=True, default=None)
    password = models.CharField(max_length=64, blank=True, null=True, default=None)
    favorite = models.ForeignKey(m.Favorite, on_delete=models.CASCADE, default=1, null=True ,blank=True)


class Purchase (models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    check = models.BooleanField(default=False)
    cash = models.BooleanField(default=True, null=True)

class Product_in_purchase(models.Model):
    id_product = models.IntegerField(null=True, default=None)
    id_purchase = models.IntegerField(null=True, default=None)
    count = models.IntegerField(null=False, default=0)