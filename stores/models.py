from django.db import models
from users.models import customer, seller


# Create your models here.

class Stores(models.Model):
    name = models.CharField(max_length=500)
    location_long = models.CharField(max_length=1000, null=True, default=45.4215)
    location_lat = models.CharField(max_length=1000, null=True, default=45.4215)
    storeimage = models.ImageField(upload_to='prim')


    def __str__(self):
        return self.name


class Products(models.Model):
    stores = models.ForeignKey(Stores, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    productimage = models.ImageField(upload_to='prim')


    def __str__(self):
        return self.name


class Orders(models.Model):
    ordernumber = models.AutoField(primary_key=True)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE, related_name='customer')
    product = models.ManyToManyField(Products, related_name='seat')
    droneid=models.CharField(max_length=1000, null=True, default=45.4215)
    start_time = models.CharField(max_length=1000, null=True)
    delivery_time = models.CharField(max_length=1000, null=True)
    status = models.CharField(max_length=1000, null=True)


    def __str__(self):
        return self.ordernumber

class drones(models.Model):
    orders = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)
    drone_long = models.CharField(max_length=1000, null=True, default=45.4215)
    drone_lat = models.CharField(max_length=1000, null=True, default=45.4215)
    dronename=models.CharField(max_length=1000, null=True, default=45.4215)

    def __str__(self):
        return self.name



from django.db import models

# Create your models here.
