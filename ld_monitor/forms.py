from . models import  subd, settings_app,urlData, methodData, connect_to_server, Category
from django.forms import ModelForm, TextInput, Select, ChoiceField, ModelChoiceField

class connectForm(ModelForm):
    class Meta:
        model = connect_to_server
        con_cat = ModelChoiceField(queryset=Category.objects.all(), empty_label='fffff', to_field_name='cat')
        fields = ['servaddr','login', 'paswd', 'cat']
        widgets ={
            'servaddr':TextInput(attrs={
                'placeholder':'Адрес сервера',
                'style':'-moz-placeholder'
            }),
            'login': TextInput(attrs={
                'placeholder': 'Доменный логин'
            }),
            'paswd': TextInput(attrs={
                'type':'password',
                'placeholder': 'Пароль'
            }),


        }
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets ={
            'name':TextInput(attrs={
                'placeholder':'название категории',
                'style':'-moz-placeholder'}),


        }

class SubdForm(ModelForm):
    class Meta:
        model = subd
        fields = ['subdaddr', 'username', 'password']
        widgets = {
            'subdaddr': TextInput(attrs={
                'placeholder': 'Адрес сервера',
                'style': '-moz-placeholder'
            }),
            'username': TextInput(attrs={
                'placeholder': 'Логин в СУБД'
            }),
            'password': TextInput(attrs={
                'type': 'password',
                'placeholder': 'Пароль'
            })
        }

class setting_form(ModelForm):
    class Meta:
        model = settings_app
        fields = ['update_period']
        widgets = {
            'update_period': TextInput(attrs={
                'placeholder': 'Введите время обновления данных в секундах.'
            })
        }

class add_url(ModelForm):
    class Meta:
        model = urlData
        fields = ['url', 'login','passwd']
        widgets = {
            'url': TextInput(attrs={'placeholder':'Введите адрес веб-клиента'}),
            'login': TextInput(attrs={
                'placeholder': 'Логин в ЛД'
            }),
            'passwd': TextInput(attrs={

                'type': 'password',
                'placeholder':'Пароль'

            })

        }

class add_method_form(ModelForm):
    class Meta:
        model = methodData
        fields = ['name_method', 'method']
        widgets = {
            'name_method': TextInput(attrs={'placeholder':'Введите наименование метода'}),
            'method': TextInput(attrs={'placeholder': 'Введите url метода'})

        }
