from django.db import models

# Create your models here.


class Inventory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    batch = models.CharField(max_length = 100)
    stock = models.IntegerField()
    deal = models.IntegerField()
    free = models.IntegerField()
    mrp = models.FloatField()
    rate = models.FloatField()
    exp = models.DateField()
    company = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)