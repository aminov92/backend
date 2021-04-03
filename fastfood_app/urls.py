from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fastfood_app import views

urlpatterns = [
    path('User/', views.UserList.as_view()),
    path('User/<int:pk>/', views.UserDetail.as_view()),
    path('Produit/', views.ProduitList.as_view()),
    path('Produit/<int:pk>/', views.ProduitDetail.as_view()),
    path('Categorie/', views.CategorieList.as_view()),
    path('Categorie/<int:pk>/', views.CategorieDetail.as_view()),
    path('Type/', views.TypeList.as_view()),
    path('Type/<int:pk>/', views.TypeDetail.as_view()),
    path('Caisse/', views.CaisseList.as_view()),
    path('Caisse/<int:pk>/', views.CaisseDetail.as_view()),
    path('Commande/', views.CommandeList.as_view()),
    path('Commande/<int:pk>/', views.CommandeDetail.as_view()),
    path('Emplacement/', views.EmplacementList.as_view()),
    path('Emplacement/<int:pk>/', views.EmplacementDetail.as_view()),
    path('LigneCommande/', views.LigneCommandeList.as_view()),
    path('LigneCommande/<int:pk>/', views.LigneCommandeDetail.as_view()),
]