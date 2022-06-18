from django.db import models


class Client(models.Model):
    name = models.CharField('ФИО', max_length=40, blank=True)
    birthday = models.DateField('День рождения', blank=True, null=True)
    phone_number = models.IntegerField('Телефон', blank=True)
    occupation = models.CharField('Профессия', max_length=40, blank=True)
    address = models.CharField('Домашний адрес', max_length=40, blank=True)
    sales_number = models.IntegerField('Кол-во продаж')
    sales_value = models.IntegerField('Сумма продаж')
    debt = models.IntegerField('Задолженность', default=0)
    notes = models.TextField('Заметки', max_length=300, blank=True)

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
    product_spendings = models.IntegerField('Расходы на продукцию', default=0)
    order_making_spendings = models.IntegerField('Расходы на оформление заказов', default=0)
    gasoline_spendings = models.IntegerField('Транспортные расходы', default=0)
    delivery_spendings = models.IntegerField('Расходы на доставку продукции', default=0)
    other_spendings = models.IntegerField('Прочие расходы', default=0)
    income = models.IntegerField('Доходы', default=0)
    date = models.DateField('Дата', auto_created=True, auto_now=True)

    def count_spendings(self):
        return self.product_spendings + self.order_making_spendings + self.gasoline_spendings + self.other_spendings


class Product(models.Model):
    TYPES = ((1, 'Уход за кожей TimeWise® Age Minimize 3D'),
             (2, 'Уход за кожей TimeWise Repair'),
             (3, 'Уход за кожей Botanical Effects'),
             (4, 'Уход за кожей Clear Proof'),
             (5, 'Уход за кожей Naturally'),
             (6, 'Коллекция MKMEN'),
             (7, 'Дополнительные средства'),
             (8, 'Аксессуары / Компактные футляры'),
             (9, 'Косметические кисти'),
             (10, 'Идеальный тон'),
             (11, 'Румяна / Контуринг'),
             (12, 'Брови'),
             (13, 'Глаза'),
             (14, 'Губы'),
             (15, 'Тело'),
             (16, 'Парфюм'),
             (17, 'Секция 2'),
             (18, 'Бонусы / подарки'))

    name = models.CharField('Наименование ', max_length=50)
    product_type = models.IntegerField('Тип', choices=TYPES, default=1)
    price = models.IntegerField('Стоимость', default=0)
    exp_date = models.DateField('Срок годности')
    sold = models.BooleanField('Куплено', default=False)

    def __str__(self):
        return f'{self.name} ({self.exp_date}) Цена: {self.price} руб.'

    def type_string(self):
        return Product.TYPES[self.product_type-1][1]


class Order(models.Model):
    product1 = models.ManyToManyField(Product, related_name='Прод1')
    product2 = models.ManyToManyField(Product, related_name='Прод2')
    product3 = models.ManyToManyField(Product, related_name='Прод3')
    product4 = models.ManyToManyField(Product, related_name='Прод4')
    product5 = models.ManyToManyField(Product, related_name='Прод5')
    product6 = models.ManyToManyField(Product, related_name='Прод6')
    product7 = models.ManyToManyField(Product, related_name='Прод7')
    product8 = models.ManyToManyField(Product, related_name='Прод8')
    product9 = models.ManyToManyField(Product, related_name='Прод9')
    product10 = models.ManyToManyField(Product, related_name='Прод10')
    product11 = models.ManyToManyField(Product, related_name='Курс11')
    product12 = models.ManyToManyField(Product, related_name='Прод12')
    product13 = models.ManyToManyField(Product, related_name='Прод13')
    product14 = models.ManyToManyField(Product, related_name='Прод14')
    product15 = models.ManyToManyField(Product, related_name='Прод15')
    product16 = models.ManyToManyField(Product, related_name='Прод16')
    product17 = models.ManyToManyField(Product, related_name='Прод17')
    product18 = models.ManyToManyField(Product, related_name='Прод18')
    customer = models.ForeignKey(Client, related_name='Покупатель', on_delete=models.DO_NOTHING)
    credit = models.IntegerField('Сумма отложенного платежа', default=0)
    date = models.DateField('Дата публикации', auto_created=True, auto_now=True)

    def sum(self):
        x = 0
        for product in self.product1.all():
            x += product.price
        for product in self.product2.all():
            x += product.price
        for product in self.product3.all():
            x += product.price
        for product in self.product4.all():
            x += product.price
        for product in self.product5.all():
            x += product.price
        for product in self.product6.all():
            x += product.price
        for product in self.product7.all():
            x += product.price
        for product in self.product8.all():
            x += product.price
        for product in self.product9.all():
            x += product.price
        for product in self.product10.all():
            x += product.price
        for product in self.product11.all():
            x += product.price
        for product in self.product12.all():
            x += product.price
        for product in self.product13.all():
            x += product.price
        for product in self.product14.all():
            x += product.price
        for product in self.product15.all():
            x += product.price
        for product in self.product16.all():
            x += product.price
        for product in self.product17.all():
            x += product.price
        for product in self.product18.all():
            x += product.price
        return x
