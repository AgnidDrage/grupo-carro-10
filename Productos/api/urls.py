from django.urls import path
from django.urls.resolvers import URLPattern
from .views import distributorView, productsView

urlpatterns = [
    path('products/', productsView.as_view(), name='product_list'),
    path('products/<int:id>', productsView.as_view(), name='product_process'),
    path('distributors/', distributorView.as_view(), name='distributor_list'),
    path('distributors/<int:id>', distributorView.as_view(), name='distributor_process'),
]