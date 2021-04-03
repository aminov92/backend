from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_nom= models.CharField(max_length=250)
    user_pseudo= models.CharField(max_length=250)
    user_password= models.CharField(max_length=250)
    caisse_default= models.CharField(max_length=250)

class Produit(models.Model):
    produit_id = models.AutoField(primary_key=True)
    prduit_nom = models.CharField(max_length=250)
    produit_prix = models.CharField(max_length=250)

class Categorie(models.Model):
    categorie_id = models.AutoField(primary_key=True)
    categorie_des = models.CharField(max_length=250)

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_des = models.CharField(max_length=250)

class Caisse(models.Model):
    caisse_id = models.AutoField(primary_key=True)
    caisse_des = models.CharField(max_length=250)

class Commande(models.Model):
    commande_id = models.AutoField(primary_key=True)
    commande_num = models.CharField(max_length=250)

class Emplacement(models.Model):
    emplacement_id = models.AutoField(primary_key=True)
    emplacement_des = models.CharField(max_length=250)

class LigneCommande(models.Model):
    lignecommande_id= models.AutoField(primary_key=True)
    commande_id = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit_id = models.ForeignKey(Produit, on_delete=models.CASCADE)
    prix = models.CharField(max_length=250)
    quantity= models.CharField(max_length=250)
    diviser_par=models.CharField(max_length=250)

def str(self):
        return self.name
