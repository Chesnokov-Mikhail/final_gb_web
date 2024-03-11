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
    image = forms.ImageField(label='Изображение блюда', widget=MyClearableFileInput)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select(), label='Выберите автора', to_field_name="id", empty_label=None)
    categories = forms.ModelMultipleChoiceField(queryset=CategorieRecipe.objects.all(), widget=forms.SelectMultiple(),
                                                 label='Выберите категории', to_field_name="id")