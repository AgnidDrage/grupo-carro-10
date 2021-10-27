from django.db import models

# Create your models here.

class Usuario(models.Model):
    user = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.user

class ProductoComprado(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    idOriginalProduct = models.IntegerField()
    salePrice = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Venta(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ProductList = models.ManyToManyField(ProductoComprado)
    sellDate = models.DateTimeField(auto_now_add=True)
    totalSellPrice = models.IntegerField()

    def __str__(self):
        return str(self.user) + " " + str(self.sellDate)

class carrosCompra(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ProductList = models.ManyToManyField(ProductoComprado)
    quantity = models.IntegerField()
    totalPrice = models.IntegerField()

