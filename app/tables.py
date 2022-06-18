import django_tables2 as tables
from .models import Client, MoneyFlow


class ClientTable(tables.Table):
    class Meta:
        model = Client
        attrs = {'class': 'paleblue'}


class MyMoneyTable(tables.Table):
    class Meta:
        model = MoneyFlow
        attrs = {'class': 'paleblue'}
