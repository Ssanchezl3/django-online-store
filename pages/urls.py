from django.urls import path
from .views import ProductIndexView, ProductShowView, ProductListView, ProductCreateView
from django.views.generic import TemplateView

urlpatterns = [
    path('', ProductIndexView.as_view(), name='product_index'),
    path('<int:id>/', ProductShowView.as_view(), name='product_show'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('created/', ProductIndexView.as_view(), name='product-created'),  # Redirect here after creation

    # Simple success page after creation
    path('created/', TemplateView.as_view(template_name='products/created.html'), name='product-created'),
]
