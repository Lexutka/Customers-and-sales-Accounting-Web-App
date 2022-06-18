from .models import Client,Product,Order
from django.forms import ModelForm, TextInput, NumberInput,DateInput,URLInput,HiddenInput,MultipleChoiceField,CheckboxInput,formset_factory
from django.forms.widgets import Select,SelectMultiple


class ClientForm(ModelForm):

    class Meta:
        model = Client
        fields = ['id_link','name', 'birthday','occupation','sales_number','sales_value','debt','notes']
        widgets = {'name': TextInput(attrs={
           'class': 'form-control',
           'placeholder': 'Введите ФИО'

        }),'id_link': HiddenInput(attrs={
            'class': 'form-control',
            'placeholder': 'дд.мм.гггг',

        }),'birthday': DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'дд.мм.гггг',

        }),'occupation': TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }),'sales_number': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'sales_value': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'debt': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }), 'notes': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'дополнительная информация о клиенте',

        })}


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['id_link','name', 'product_type','price','exp_date','sold']
        widgets = {'name': TextInput(attrs={
           'class': 'form-control',
           'placeholder': ''

        }),'id_link': HiddenInput(attrs={
            'class': 'form-control',
            'placeholder': 'дд.мм.гггг',

        }),'product_type': TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }),'price': NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '',

        }),'exp_date': DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'дд.мм.гггг',

        }), 'sold': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'дд.мм.гггг'
        })}

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product','customer']
        widgets = {'product': SelectMultiple(attrs={
           'class': 'form-control',
           'placeholder': ''

        }),'customer': Select(attrs={
            'class': 'form-control',
            'placeholder': '',

        })}

