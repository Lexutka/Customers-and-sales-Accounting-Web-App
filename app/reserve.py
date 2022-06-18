{% extends 'templatepage.html' %}

{%block title %}
Новый заказ
{%endblock%}

{%block content%}
<form method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit" class="btn btn-success">Добавить товар</button>
</form>
{%endblock%}

def new_order(request):
    if request.method == 'POST':
        products = OrderForm(request.POST)
        if products.is_valid():
            products.save()
            order = Order.objects.last()
            count_an_income(order)
            client_order(order)
            new_sale_pop()
        return redirect('home')
    form = OrderForm()
    context = {
        'form':form,
    }
    return render(request,'new_order.html',context)


def list_of_orders(request):
    return render(request,'orderlist.html',{'orders': Order.objects.all()})



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product','customer']
        widgets = {'product': SelectMultiple(attrs={
           'class': 'form-control',
           'placeholder': '',
            'type':'checkbox'

        }),'customer': Select(attrs={
            'class': 'form-control',
            'placeholder': '',

        })}

    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(sold=False)


 TYPES = (
        'Уход за кожей TimeWise® Age Minimize 3D',
        'Уход за кожей TimeWise Repair',
        'Уход за кожей Botanical Effects',
        'Уход за кожей Clear Proof',
        'Уход за кожей Naturally',
        'Коллекция MKMEN',
        'Дополнительные средства',
        'Аксессуары / Компактные футляры',
        'Косметические кисти',
        'Идеальный тон',
        'Румяна / Контуринг',
        'Брови',
        'Глаза',
        'Губы',
        'Тело',
        'Парфюм',
        'Секция 2',
        'Бонусы / подарки',
    )
,choices=TYPES

class Product(models.Model):
    TYPES = ((1,('Уход за кожей TimeWise® Age Minimize 3D')),
        (2,('Уход за кожей TimeWise Repair')),
        (3,('Уход за кожей Botanical Effects')),
        (4,('Уход за кожей Clear Proof')),
        (5,('Уход за кожей Naturally')),
        (6,('Коллекция MKMEN')),
        (7,('Дополнительные средства')),
        (8,('Аксессуары / Компактные футляры')),
        (9,('Косметические кисти')),
        (10,('Идеальный тон')),
        (11,('Румяна / Контуринг')),
        (12,('Брови')),
        (13,('Глаза')),
        (14,('Губы')),
        (15,('Тело')),
        (16,('Парфюм')),
        (17,('Секция 2)'),
        (18,('Бонусы / подарки'))))

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

    class OrderForm(ModelForm):
        class Meta:
            model = Order
            fields = ['product', 'customer']
            product = ModelMultipleChoiceField(queryset=Product.objects.all(), required=False,
                                               widget=CheckboxSelectMultiple)

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            self.fields['product'].queryset = Product.objects.filter(sold=False)

            def new_order(request):
                products = Product.objects.all()
                if request.method == 'POST':
                    products = OrderForm(request.POST)
                    if products.is_valid():
                        products.save()
                        order = Order.objects.last()
                        count_an_income(order)
                        client_order(order)
                        new_sale_pop(order)
                    return redirect('home')
                form = OrderForm()
                context = {
                    'form': form,
                    'products': products,
                }
                return render(request, 'new_order.html', context)


    class Meta:
        fields = [
            'name', 'birthday', 'phone_number',
            'occupation', 'address', 'sales_number',
            'sales_value', 'debt', 'notes'
            ]
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'maxlength': '40',
            'placeholder': 'Введите ФИО'

        }), 'birthday': DateInput(attrs={
            'class': 'form-control',
            'type': 'text',
            'onfocus': '(this.type="date")',
            'onblur': '(this.type="text")',
            'placeholder': 'дд.мм.гггг',
            'required': True,
            'error_css_class': 'error',

        }), 'phone_number': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '7-XXX-XXX-XX-XX',
            'type': 'tel',
            'pattern': '+7[0-9]{3}[0-9]{3}[0-9]{2}[0-9]{2}',

        }), 'occupation': TextInput(attrs={
            'class': 'form-control',
            'maxlength': '40',
            'placeholder': 'Место работы',

        }), 'address': TextInput(attrs={
            'class': 'form-control',
            'maxlength': '40',
            'placeholder': 'Место проживания',

        }), 'sales_number': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'sales_value': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'debt': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'notes': Textarea(attrs={
            'class': 'form-control notes',
            'maxlength': '300',
            'placeholder': 'дополнительная информация о клиенте',

        })}

        class ProductForm(ModelForm):
            class Meta:
                model = Product
                product_type = MultipleChoiceField(choices=Product.TYPES, widget=CheckboxSelectMultiple())
                fields = ['name', 'product_type', 'price', 'exp_date', 'sold']
                widgets = {'name': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Название продукта',

                }), 'product_type': Select(attrs={
                    'class': 'form-control',
                    'placeholder': '',

                }), 'price': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': '',

                }), 'exp_date': DateInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'дд.мм.гггг',
                    'type': 'date'

                }), 'sold': CheckboxInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'дд.мм.гггг'
                })}

        class OrderForm(ModelForm):
            product1 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=1, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product2 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=2, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product3 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=3, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product4 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=4, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product5 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=5, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product6 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=6, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product7 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=7, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product8 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=8, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product9 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=9, sold=False),
                                                required=False, widget=CheckboxSelectMultiple)
            product10 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=10, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product11 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=11, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product12 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=12, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product13 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=13, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product14 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=14, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product15 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=15, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product16 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=16, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product17 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=17, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)
            product18 = ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=18, sold=False),
                                                 required=False, widget=CheckboxSelectMultiple)

            class Meta:
                model = Order
                prod = Product.objects.filter(sold=False)
                fields = '__all__'

        class MoneyFlowForm(ModelForm):
            class Meta:
                model = MoneyFlow
                fields = ['product_spendings', 'order_making_spendings',
                          'gasoline_spendings', 'other_spendings',
                          'delivery_spendings', 'income']
                widgets = {'product_spendings': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': ''

                }), 'order_making_spendings': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': ''

                }), 'gasoline_spendings': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': ''

                }), 'other_spendings': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': ''

                }), 'income': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': ''

                }), 'delivery_spendings': NumberInput(attrs={
                    'class': 'form-control',
                    'placeholder': ''

                })}

                def client_order(order):
                    bought = order.customer.sales_value
                    bought = count_order_price(bought, order)
                    number = order.customer.sales_number + 1
                    order.customer.sales_number = number
                    order.customer.sales_value = bought
                    order.customer.save()