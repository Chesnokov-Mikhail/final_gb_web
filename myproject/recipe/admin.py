from django.contrib import admin
from .models import Recipe, CategorieRecipe, Product, Author

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'registration_date']
    ordering = ['name', 'registration_date']
    list_filter = ['registration_date']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'add_date']
    ordering = ['name', 'add_date']
    list_filter = ['add_date']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описания (description)'

@admin.register(CategorieRecipe)
class CategorieRecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    ordering = ['title']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описания (description)'