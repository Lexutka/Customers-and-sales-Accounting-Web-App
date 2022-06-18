from django.shortcuts import render, redirect
from .forms import ClientForm, ProductForm, OrderForm, MoneyFlowForm
from .models import Client, Product, MoneyFlow, Order
from .finfunc import new_sale_pop, count_income, count_spendings, count_an_income, client_order, client_debt_new
from django import forms


def index(request):
    return render(request, 'home.html')


def new_client(request):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST)
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
    return render(request, 'new_client.html', context)


def list_of_products(request):
    products = Product.objects.filter(sold=False)
    context = {'products': products}
    return render(request, 'productlist.html', context)


def new_product(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product = Product.objects.last()
            init_price = round(product.price*0.55)
            new_flow = MoneyFlowForm({'income': 0,
                                      'product_spendings': init_price,
                                      'order_making_spendings': 0,
                                      'delivery_spendings': 0,
                                      'gasoline_spendings': 0,
                                      'other_spendings': 0
                                      })
            if new_flow.is_valid():
                new_flow.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'new_product.html', context)


def list_of_clients(request):
    order_by = request.GET.get('order_by', 'name')
    clients = Client.objects.all().order_by(order_by)
    context = {'clients': clients, 'order_by': order_by}
    return render(request, 'clientlist.html', context)


def clientpage(request, x):
    post = Client.objects.get(pk=x)
    form = ClientForm(instance=post)
    error = ''
    if request.method == "POST":
        form = ClientForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно. Скорее всего, не заполнена дата рождения'
    context = {'form': form, 'error': error}
    return render(request, 'clientpage.html', context)


def productpage(request, x):
    post = Product.objects.get(pk=x)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('home')
    else:
        form = ProductForm(instance=post)
    context = {'form': form,
               'post': post
               }
    return render(request, 'productpage.html', context)


def money_page(request):
    order_by = request.GET.get('order_by', 'date')
    flows = MoneyFlow.objects.all().order_by(order_by)
    income = count_income(MoneyFlow)
    spendings = count_spendings(MoneyFlow)
    profit = income - spendings
    context = {'flows': flows,
               'order_by': order_by,
               'minus': spendings,
               'income': income,
               'profit': profit
               }
    return render(request, 'moneypage.html', context)


def new_order(request):
    products = Product.objects.all()
    order_sum = 0
    if request.method == 'POST':
        products = OrderForm(request.POST)
        if products.is_valid():
            products.save()
            order = Order.objects.last()
            count_an_income(order)
            client_order(order)
            client_debt_new(order)
            new_sale_pop(order)
            return redirect('home')
    form = OrderForm()
    context = {
        'form': form,
        'products': products,
        }
    return render(request, 'new_order.html', context)


def list_of_orders(request):
    context = {'orders': Order.objects.all()}
    return render(request, 'orderlist.html', context)


def orderpage(request, x):
    order = Order.objects.get(pk=x)
    context = {'order': order}
    return render(request, 'orderpage.html', context)


def new_spending(request):
    if request.method == 'POST':
        form = MoneyFlowForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    form = MoneyFlowForm({'income': 0, 'product_spendings': 0,
                        'order_making_spendings': 0, 'gasoline_spendings': 0,
                        'other_spendings': 0, 'delivery_spendings': 0
                          })
    context = {
        'form': form
    }
    return render(request, 'new_spending.html', context)


def delete_product(request, x):
    Product.objects.filter(id=x).delete()
    return redirect('products')
