from django import forms
from django.forms.widgets import ClearableFileInput
import datetime
from .models import Product, CategorieRecipe, Recipe, Author

class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = 'Изменить изображение'
    clear_checkbox_label = 'Удалить изображение'

class TimePickerInput(forms.TimeInput):
        input_type = 'time'
class AddEditRecipe(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, label='Наименование рецепта')
    description = forms.CharField(required=False, widget=forms.Textarea(), label='Описание блюда')
    ingredients = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.SelectMultiple(),
                                                 label='Выберите ингредиенты', to_field_name="id")
    cooking_steps = forms.CharField(required=False, widget=forms.Textarea(), label='Пошаговое описание приготовления')
    cooking_time = forms.TimeField(widget=TimePickerInput(format='%H:%M'), label='Время приготовления')
    image = forms.ImageField(required=False, label='Изображение блюда', widget=MyClearableFileInput)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select(), label='Выберите автора', to_field_name="id")
    categories = forms.ModelMultipleChoiceField(queryset=CategorieRecipe.objects.all(), widget=forms.SelectMultiple(),
                                                 label='Выберите категории', to_field_name="id")
    modify_date = forms.DateTimeField(initial=datetime.datetime.now(), disabled=True, label='Дата изменения')

class AddEditAuthor(forms.Form):
    name = forms.CharField(min_length=3, max_length=100, label='Имя автора')
    email = forms.EmailField(label='Электронная почта', max_length=100,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'user@mail.ru'}))
    registration_date = forms.DateField(disabled=True, initial=datetime.date.today,
                                        label='Дата регистрации')

class AddEditProduct(forms.Form):
    name = forms.CharField(min_length=3, max_length=200, label='Название продукта')
    description = forms.CharField(required=False, widget=forms.Textarea(), label='Описание продукта')
    add_date = forms.DateField(disabled=True, initial=datetime.date.today,
                                        label='Дата добавления продукта')

class AddEditCategorieRecipe(forms.Form):
    title = forms.CharField(min_length=3, max_length=100, label='Название категории')
    description = forms.CharField(required=False, widget=forms.Textarea(), label='Описание категории')