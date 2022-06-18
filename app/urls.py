from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^clients/(?P<x>\d+)', views.clientpage, name='clientpage'),
    re_path(r'^clients', views.list_of_clients, name='clients'),
    re_path(r'^products/delete/(?P<x>\d+)', views.delete_product),
    re_path(r'^products/(?P<x>\d+)', views.productpage, name='productpage'),
    re_path(r'^products', views.list_of_products, name='products'),
    re_path(r'^orders/(?P<x>\d+)', views.orderpage, name='orderpage'),
    re_path(r'^orders', views.list_of_orders, name='orders'),
    re_path(r'^newby', views.new_client, name='newby'),
    re_path(r'^new_product', views.new_product, name='new_product'),
    re_path(r'^new_order', views.new_order, name='new_order'),
    re_path(r'^mymoney', views.money_page, name='moneypage'),



    path('products/delete/<x>', views.delete_product, name='delete_product'),
    path('new_spending', views.new_spending, name='new_spending'),
]
