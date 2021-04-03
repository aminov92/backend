from django.contrib import admin
from django.urls import path, include
import fastfood_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fastfood_app.urls')),
]
