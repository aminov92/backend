from django.contrib import admin
from . models import *

# Register your models here.

admin.register(Produit, Categorie, Type, Caisse, Commande, Emplacement, LigneCommande)(admin.ModelAdmin)




