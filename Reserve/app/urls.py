from django.urls import path
from . import views
from .models import Client

urlpatterns = [
    path('', views.index,name='home'),
    path('clients',views.list_of_clients,name='clients'),
    path('products', views.list_of_products, name='products'),
    path('orders', views.list_of_orders, name='orders'),
    path('newby',views.new_client,name='newby'),
    path('new_product',views.new_product,name='new_product'),
    path('sale',views.new_sale,name='sale'),
    path('mymoney',views.money_page,name='moneypage'),
    path('<x>',views.redirect_pages,name='clientpage'),
    path('clients/<x>',views.clientpage,name='clientpage'),
    path('products/<x>',views.productpage,name='clientpage'),
]