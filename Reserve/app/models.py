import datetime
import random

from django.db import models


class Client(models.Model):
    name = models.CharField('ФИО',max_length=40,blank=True)
    id_link = models.URLField('Ссылка на профиль',default='',auto_created=True,unique=True,primary_key=True)
    birthday = models.DateField('День рождения',default='11.11.1111',blank=True)
    occupation = models.CharField('Профессия',max_length=20,blank=True)
    sales_number = models.IntegerField('Кол-во продаж',default=0)
    sales_value = models.IntegerField('Сумма продаж',default=0)
    debt = models.IntegerField('Задолженность',default=0)
    notes = models.TextField('Заметки',max_length=300,blank=True)

    def __str__(self):
        return self.name

    def new_order(self,):
        pass

    def new_interaction(self):
        pass

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    @classmethod
    def request_client(cls):
        cls.name = "<p>{{ name }}</p>"


class MoneyFlow(models.Model):
    product_spendings = models.IntegerField('Расходы на продукцию',default=0)
    order_making_spendings = models.IntegerField('Расходы на оформление заказов',default=0)
    gasoline_spendings = models.IntegerField('Транспортные расходы',default=0)
    other_spendings = models.IntegerField('Прочие расходы',default=0)
    total_spendings = models.IntegerField('Общие расходы',default=0)
    income = models.IntegerField('Доходы',default=0)
    disc_profit = models.IntegerField('Прибыль (с вычетом спецпредложений)',default=0)
    gen_profit = models.IntegerField('Прибыль (общая)',default=0)

    def new_spending(self):
        pass

    def monthly_report(self):
        pass


class Product(models.Model):
    name = models.CharField('Наименование ',max_length=50)
    id_link = models.URLField('Ссылка на страницу товара', default='', auto_created=True, unique=True, primary_key=True)
    product_type = models.CharField('Тип',max_length=30,blank=True)
    price = models.IntegerField('Стоимость',default=0)
    exp_date = models.DateField('Срок годности')
    sold = models.BooleanField('Куплено',default=False)

    def __str__(self):
        return f'{self.name} ({self.exp_date})'


class Order(models.Model):
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(Client,related_name='Покупатель',on_delete=models.CASCADE)

def new_sale_pop():
    for order in Order.objects.all():
        for sold_product in order.product.all():
            sold_product.sold = True
            sold_product.save()


def new_order_income():
    for product in Product.objects.filter(sold=True):
        product.price
