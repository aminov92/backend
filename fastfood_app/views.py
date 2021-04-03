from rest_framework import generics
from .import models
from .import serializers

class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class ProduitList(generics.ListCreateAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = serializers.ProduitSerializer
class ProduitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Produit.objects.all()
    serializer_class = serializers.ProduitSerializer

class CategorieList(generics.ListCreateAPIView):
    queryset = models.Categorie.objects.all()
    serializer_class = serializers.CategorieSerializer
class CategorieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categorie.objects.all()
    serializer_class = serializers.CategorieSerializer

class TypeList(generics.ListCreateAPIView):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer

class CaisseList(generics.ListCreateAPIView):
    queryset = models.Caisse.objects.all()
    serializer_class = serializers.CaisseSerializer
class CaisseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Caisse.objects.all()
    serializer_class = serializers.CaisseSerializer

class CommandeList(generics.ListCreateAPIView):
    queryset = models.Commande.objects.all()
    serializer_class = serializers.CommandeSerializer
class CommandeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Commande.objects.all()
    serializer_class = serializers.CommandeSerializer

class EmplacementList(generics.ListCreateAPIView):
    queryset = models.Emplacement.objects.all()
    serializer_class = serializers.EmplacementSerializer
class EmplacementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Emplacement.objects.all()
    serializer_class = serializers.EmplacementSerializer
    
class LigneCommandeList(generics.ListCreateAPIView):
    queryset = models.LigneCommande.objects.all()
    serializer_class = serializers.LigneCommandeSerializer
class LigneCommandeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.LigneCommande.objects.all()
    serializer_class = serializers.LigneCommandeSerializer