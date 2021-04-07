from rest_framework import generics
from .import models
from .import serializers

class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class TypeList(generics.ListCreateAPIView):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer

class BoxList(generics.ListCreateAPIView):
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer
class BoxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Box.objects.all()
    serializer_class = serializers.BoxSerializer

class BoxLogList(generics.ListCreateAPIView):
    queryset = models.BoxLog.objects.all()
    serializer_class = serializers.BoxLogSerializer
class BoxLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BoxLog.objects.all()
    serializer_class = serializers.BoxLogSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderStatusList(generics.ListCreateAPIView):
    queryset = models.OrderStatus.objects.all()
    serializer_class = serializers.OrderStatusSerializer
class OrderStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OrderStatus.objects.all()
    serializer_class = serializers.OrderStatusSerializer

class LocationList(generics.ListCreateAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    
class OrderLigneList(generics.ListCreateAPIView):
    queryset = models.OrderLigne.objects.all()
    serializer_class = serializers.OrderLigneSerializer
class OrderLigneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.OrderLigne.objects.all()
    serializer_class = serializers.OrderLigneSerializer

class KitchenList(generics.ListCreateAPIView):
    queryset = models.Kitchen.objects.all()
    serializer_class = serializers.KitchenSerializer
class KitchenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Kitchen.objects.all()
    serializer_class = serializers.KitchenSerializer