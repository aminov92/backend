from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    product_price = models.CharField(max_length=250)

class Category(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_des = models.CharField(max_length=250)

class Type(models.Model):
    type_des = models.CharField(max_length=250)

class Box(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    box_des = models.CharField(max_length=250)

class BoxLog(models.Model):
    box_id = models.ForeignKey(Box, on_delete=models.CASCADE)
    expenses = models.CharField(max_length=250)

class Order(models.Model):
    box_id = models.ForeignKey(Box, on_delete=models.CASCADE)
    order_num = models.CharField(max_length=250)

class Location(models.Model):
    location_des = models.CharField(max_length=250)

class OrderLigne(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.CharField(max_length=250)
    quantity= models.CharField(max_length=250)
    divide_by=models.CharField(max_length=250)

class OrderStatus(models.Model):
    status_des = models.CharField(max_length=250)

class Kitchen(models.Model):
    kitchen_des = models.CharField(max_length=250)
    printer_ip = models.CharField(max_length=250)

def str(self):
        return self.name
