from django.contrib import admin
from . models import *

# Register your models here.

admin.register(Product, Category, Type, Box, BoxLog, Order, Location, OrderLigne, OrderStatus, Kitchen)(admin.ModelAdmin)




