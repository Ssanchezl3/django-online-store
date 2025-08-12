from django.urls import path
from .views import (
    ProductIndexView,
    ProductShowView,
    ProductListView,
    ProductCreateView,
    CartView,
    CartRemoveAllView
)
from django.views.generic import TemplateView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='product_index'),
    path('<int:id>/', ProductShowView.as_view(), name='product_show'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),

    # Página de éxito después de crear un producto
    path('created/', TemplateView.as_view(template_name='products/created.html'), name='product-created'),

    # -------------------
    # Rutas para el carrito
    # -------------------
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
]
