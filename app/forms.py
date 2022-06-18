from .models import Client, Product, Order, MoneyFlow
from django import forms


class ClientForm(forms.ModelForm):
    name = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'maxlength': '40',
                            'placeholder': 'Введите ФИО'
                            }))
    birthday = forms.DateField(
                            widget=forms.DateInput(attrs={
                            'class': 'form-control',
                            'type': 'text',
                            'onfocus': '(this.type="date")',
                            'onblur': '(this.type="text")',
                            'placeholder': 'дд.мм.гггг',
                            'error_css_class': 'error',
                            'required': 'False',
                            }))
    phone_number = forms.IntegerField(
                            required=False,
                            widget=forms.NumberInput(attrs={
                            'class': 'form-control',
                            'placeholder': '7-XXX-XXX-XX-XX',
                            'type': 'tel',
                            'pattern': '+7[0-9]{3}[0-9]{3}[0-9]{2}[0-9]{2}',
                            }))
    occupation = forms.CharField(
                            required=False,
                            widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'maxlength': '40',
                            'placeholder': 'Место работы',
                            }))
    address = forms.CharField(
                            required=False,
                            widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'maxlength': '40',
                            'placeholder': 'Место проживания',
                            }))
    sales_number = forms.IntegerField(
                            initial=0,
                            widget=forms.NumberInput(attrs={
                            'class': 'form-control',
                            'placeholder': '',
                            }))
    sales_value = forms.IntegerField(
                            initial=0,
                            widget=forms.NumberInput(attrs={
                            'class': 'form-control',
                            }))
    debt = forms.IntegerField(
                            initial=0,
                            widget=forms.NumberInput(attrs={
                            'class': 'form-control',
                            }))
    notes = forms.CharField(
                            required=False,
                            widget=forms.Textarea(attrs={
                            'class': 'form-control notes',
                            'maxlength': '300',
                            'placeholder': 'дополнительная информация о клиенте',
                            }))

    class Meta:
        model = Client
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        product_type = forms.MultipleChoiceField(choices=Product.TYPES, widget=forms.CheckboxSelectMultiple())
        fields = ['name', 'product_type', 'price', 'exp_date', 'sold']
        widgets = {'name': forms.TextInput(attrs={
           'class': 'form-control',
           'placeholder': 'Название продукта',

        }), 'product_type': forms.Select(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'price': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'exp_date': forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'дд.мм.гггг',
            'type': 'date'

        }), 'sold': forms.CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг'
        })}


class OrderForm(forms.ModelForm):
    product1 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=1, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product2 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=2, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product3 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=3, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product4 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=4, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product5 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=5, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product6 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=6, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product7 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=7, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product8 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=8, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product9 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=9, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product10 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=10, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product11 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=11, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product12 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=12, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product13 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=13, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product14 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=14, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product15 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=15, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product16 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=16, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product17 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=17, sold=False), required=False, widget=forms.CheckboxSelectMultiple)
    product18 = forms.ModelMultipleChoiceField(queryset=Product.objects.filter(product_type=18, sold=False), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Order
        prod = Product.objects.filter(sold=False)
        fields = '__all__'


class MoneyFlowForm(forms.ModelForm):
    class Meta:
        model = MoneyFlow
        fields = ['product_spendings', 'order_making_spendings',
                  'gasoline_spendings', 'other_spendings',
                  'delivery_spendings', 'income']
        widgets = {'product_spendings': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''

        }), 'order_making_spendings': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''

        }), 'gasoline_spendings': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''

        }), 'other_spendings': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''

        }), 'income': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''

        }), 'delivery_spendings': forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': ''

        })}

