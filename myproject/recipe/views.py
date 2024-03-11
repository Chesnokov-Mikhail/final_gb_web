from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import View
from random import choices
from datetime import datetime, timedelta
from .models import Product, CategorieRecipe, Recipe, Author

# Create your views here.

class GetIndex(View):
    def get(self, request):
        recipes = choices(Recipe.objects.all(), k=5)
        result = {}
        for recipe in recipes:
            ingredients = recipe.ingredients.all()
            categories = recipe.categories.all()
            result[recipe] = {'ingredients': ingredients,
                              'categories': categories}
        title_content = 'Наши рецепты:'
        context = {'title': 'Сайт рецептов',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'recipe/index.html', context)