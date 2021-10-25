from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE)
    amount = models.IntegerField()
    quantitySold = models.IntegerField()
    
    def __str__(self):
        return self.name

class Distributor(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


