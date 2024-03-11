from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import View
from random import choices
from datetime import datetime, timedelta
from .models import Product, CategorieRecipe, Recipe, Author
from .forms import AddEditRecipe

# Create your views here.

class GetIndex(View):
    def get(self, request):
        result = {}
        recipes_queryset = Recipe.objects.all()
        if recipes_queryset:
            recipes = choices(recipes_queryset, k=5)
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

class PostRecipe(View):
    def get(self,request):
        form = AddEditRecipe()
        title_content = 'Добавление рецепта'
        context = {'title': 'Сайт рецептов',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        return render(request, 'recipe/add_recipe.html', context)

    def post(self,request):
        form = AddEditRecipe(request.POST, request.FILES)
        title_content = 'Добавление рецепта'
        message = 'Рецепт не сохранен'
        context = {'title': 'Сайт рецептов',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   }
        if form.is_valid():
            recipe = Recipe.objects.create(name=form.cleaned_data['name'],
                                description=form.cleaned_data['description'],
                                cooking_steps=form.cleaned_data['cooking_steps'],
                                cooking_time=form.cleaned_data['cooking_time'],
                                author=form.cleaned_data['author'],
                                image=form.cleaned_data['image'])
            for ingredient in form.cleaned_data['ingredients']:
                recipe.ingredients.add(ingredient)
            for categorie in form.cleaned_data['categories']:
                recipe.categories.add(categorie)
            recipe.save()
            message = 'Рецепт сохранен'
        context['message'] = message
        return render(request, 'recipe/add_recipe.html', context)