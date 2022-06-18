from .models import Order
from .forms import MoneyFlowForm, ClientForm
import re


def new_sale_pop(order):
    for prod in order.product1.all():
        prod.sold = True
        prod.save()
    for prod in order.product2.all():
        prod.sold = True
        prod.save()
    for prod in order.product3.all():
        prod.sold = True
        prod.save()
    for prod in order.product4.all():
        prod.sold = True
        prod.save()
    for prod in order.product5.all():
        prod.sold = True
        prod.save()
    for prod in order.product6.all():
        prod.sold = True
        prod.save()
    for prod in order.product7.all():
        prod.sold = True
        prod.save()
    for prod in order.product8.all():
        prod.sold = True
        prod.save()
    for prod in order.product9.all():
        prod.sold = True
        prod.save()
    for prod in order.product10.all():
        prod.sold = True
        prod.save()
    for prod in order.product11.all():
        prod.sold = True
        prod.save()
    for prod in order.product12.all():
        prod.sold = True
        prod.save()
    for prod in order.product13.all():
        prod.sold = True
        prod.save()
    for prod in order.product14.all():
        prod.sold = True
        prod.save()
    for prod in order.product15.all():
        prod.sold = True
        prod.save()
    for prod in order.product16.all():
        prod.sold = True
        prod.save()
    for prod in order.product17.all():
        prod.sold = True
        prod.save()
    for prod in order.product18.all():
        prod.sold = True
        prod.save()


def count_income(flow):
    x = 0
    for a_flow in flow.objects.all():
        x += a_flow.income
    return x


def count_order_price(order_value, order):
    for product in order.product1.all():
        order_value += product.price
    for product in order.product2.all():
        order_value += product.price
    for product in order.product3.all():
        order_value += product.price
    for product in order.product4.all():
        order_value += product.price
    for product in order.product5.all():
        order_value += product.price
    for product in order.product6.all():
        order_value += product.price
    for product in order.product7.all():
        order_value += product.price
    for product in order.product8.all():
        order_value += product.price
    for product in order.product9.all():
        order_value += product.price
    for product in order.product10.all():
        order_value += product.price
    for product in order.product11.all():
        order_value += product.price
    for product in order.product12.all():
        order_value += product.price
    for product in order.product13.all():
        order_value += product.price
    for product in order.product14.all():
        order_value += product.price
    for product in order.product15.all():
        order_value += product.price
    for product in order.product16.all():
        order_value += product.price
    for product in order.product17.all():
        order_value += product.price
    for product in order.product18.all():
        order_value += product.price
    return order_value


def count_an_income(order):
    new_income = 0
    new_income = count_order_price(new_income, order)
    new_flow = MoneyFlowForm({'income': new_income, 'product_spendings': 0,
                              'order_making_spendings': 0, 'gasoline_spendings': 0,
                              'other_spendings': 0, 'delivery_spendings': 0})
    if new_flow.is_valid():
        new_flow.save()


def count_spendings(flow):
    x = 0
    for a_flow in flow.objects.all():
        x += a_flow.product_spendings + a_flow.order_making_spendings + a_flow.gasoline_spendings + a_flow.other_spendings
    return x


def client_order(new_order):
    prev_bought = new_order.customer.sales_value
    total_bought = count_order_price(prev_bought, new_order)
    number = new_order.customer.sales_number + 1
    new_order.customer.sales_number = number
    new_order.customer.sales_value = total_bought
    new_order.customer.save()


def client_debt_new(new_order):
        new_order.customer.debt += new_order.credit
        new_order.customer.save()
