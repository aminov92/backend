from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from fastfood_app import views

urlpatterns = [
    path('Product/', views.ProductList.as_view()),
    path('Product/<int:pk>/', views.ProductDetail.as_view()),
    path('Category/', views.CategoryList.as_view()),
    path('Category/<int:pk>/', views.CategoryDetail.as_view()),
    path('Type/', views.TypeList.as_view()),
    path('Type/<int:pk>/', views.TypeDetail.as_view()),
    path('Box/', views.BoxList.as_view()),
    path('Box/<int:pk>/', views.BoxDetail.as_view()),
    path('BoxLog/', views.BoxLogList.as_view()),
    path('BoxLog/<int:pk>/', views.BoxLogDetail.as_view()),
    path('Order/', views.OrderList.as_view()),
    path('Order/<int:pk>/', views.OrderDetail.as_view()),
    path('Location/', views.LocationList.as_view()),
    path('Location/<int:pk>/', views.LocationDetail.as_view()),
    path('OrderLigne/', views.OrderLigneList.as_view()),
    path('OrderLigne/<int:pk>/', views.OrderLigneDetail.as_view()),
    path('OrderStatus/', views.OrderStatusList.as_view()),
    path('OrderStatus/<int:pk>/', views.OrderStatusDetail.as_view()),
    path('Kitchen/', views.KitchenList.as_view()),
    path('Kitchen/<int:pk>/', views.KitchenDetail.as_view()),
]