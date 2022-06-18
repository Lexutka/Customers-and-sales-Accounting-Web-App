import random

from django.http import HttpRequest,HttpResponse
from django.shortcuts import render,redirect
import datetime
from .forms import ClientForm,ProductForm,OrderForm
from .models import Client,Product,MoneyFlow,Order,new_sale_pop
from django_tables2 import RequestConfig
from .tables import ClientTable,MyMoneyTable
from django.views.generic.edit import UpdateView
from django.forms import inlineformset_factory


def index(request):
    new_sale_pop()
    return render(request,'home.html')


def new_client(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ClientForm(initial={'id_link': f'http://127.0.0.1:8000/clients/{random.randint(1000,10000)}','notes': ''})
    context = {
        'form': form,
        'error': error
    }
    return render(request,'new_client.html',context)


def list_of_products(request):
    return render(request,'productlist.html',{'products': Product.objects.all()})

def new_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            new_sale_pop()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ProductForm(initial={'id_link': f'http://127.0.0.1:8000/products/{random.randint(10001,20000)}'})
    context = {
        'form': form,
        'error': error
    }
    return render(request,'new_product.html',context)


def list_of_clients(request):
    table = ClientTable(Client.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'clientlist.html', {'table': table})


def clientpage(request,pk):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST.get(pk))
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ClientForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'clientpage.html', context)


def clientpage(request, x):
    post = Client.objects.get(pk=f'http://127.0.0.1:8000/clients/{x}')
    if request.method == "POST":
        form = ClientForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = ClientForm(instance=post)
    return render(request, 'clientpage.html', {'form': form})

def redirect_pages(request,x):
    if int(HttpRequest.readlines(x)[0])>10000:
        return redirect('products/<x>')
    else:
        return redirect('clients/<x>')


def productpage(request, x):
    post = Product.objects.get(pk=f'http://127.0.0.1:8000/products/{x}')
    if request.method == "POST":
        form = ProductForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = ProductForm(instance=post)
    return render(request, 'productpage.html', {'form': form})


def money_page(request):
    table = MyMoneyTable(MoneyFlow.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'moneypage.html', {'table': table})


def new_sale(request):
    if request.method == 'POST':
        products = OrderForm(request.POST)
        if products.is_valid():
            products.save()
            return redirect('home')
    products = Product.objects.filter(sold=False)
    form = OrderForm()
    context = {
        'form':form,
        'products': products,
    }
    return render(request,'new_order.html',context)


def list_of_orders(request):
    return render(request,'orderlist.html',{'orders': Order.objects.all()})