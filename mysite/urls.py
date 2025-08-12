from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de productos
    path('products/', include('pages.urls')),

    # Rutas directas desde raíz (incluye carrito)
    path('', include('pages.urls')),
]
