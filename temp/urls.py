from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UserView, ProductoCompradoView, VentaView


urlpatterns = [
    path('user/', UserView.as_view(), name='user-list'),
    path('user/<int:id>', UserView.as_view(), name='user-process'),
    path('productoComprado/', ProductoCompradoView.as_view(), name='productCompr_list'),
    path('productoComprado/<int:id>', ProductoCompradoView.as_view(), name='productCompr_process'),
    path('venta/', VentaView.as_view(), name='venta-list'),
    path('venta/<int:id>', VentaView.as_view(), name='venta-process'),

]