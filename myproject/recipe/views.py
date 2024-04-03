from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings
from random import choices
from datetime import datetime, timedelta
from .models import Product, CategorieRecipe, Recipe, Author

from .forms import AddEditRecipe, AddEditAuthor, AddEditProduct, AddEditCategorieRecipe

# Create your views here.

class GetCategorie(View):
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        categorie_id = kwargs.get('categorie_id',None)
        context = {'title': 'Сайт рецептов',}
        if categorie_id:
            categorie_select = CategorieRecipe.objects.get(pk=categorie_id)
            if categorie_select:
                form = AddEditCategorieRecipe(initial={'title': categorie_select.title,
                                                'description': categorie_select.description,
                                                 }
                                        )
                for key in form.fields.keys():
                    form.fields[key].disabled = True
                title_content = 'Просмотр информации по категории'
                context['read'] = form
        else:
            title_content = 'Категория не найдена'
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_categorie.html', context)

class PostCategorie(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ('recipe.view_categorierecipe',
                           'recipe.change_categorierecipe',
                           'recipe.add_categorierecipe')
    login_url = settings.LOGIN_URL
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        categorie_id = kwargs.get('categorie_id',None)
        categorie_edit = kwargs.get('edit', None)
        context = {'title': 'Сайт рецептов',}
        if categorie_id:
            categorie_select = CategorieRecipe.objects.get(pk=categorie_id)
            if categorie_select:
                form = AddEditCategorieRecipe(initial={'title': categorie_select.title,
                                                'description': categorie_select.description,
                                                 }
                                        )
                if categorie_edit:
                    title_content = 'Редактирование информации о категории'
                    context['form'] = form
        else:
            form = AddEditCategorieRecipe()
            title_content = 'Добавление категории'
            context['form'] = form
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_categorie.html', context)

    def post(self,request, **kwargs):
        form = AddEditCategorieRecipe(request.POST)
        categorie_id = kwargs.get('categorie_id', None)
        categorie_edit = kwargs.get('edit', None)
        title_content = 'Добавление категории'
        message = 'Категория не сохранена'
        if form.is_valid():
            if categorie_id and categorie_edit:
                CategorieRecipe.objects.filter(pk=categorie_id).update(title=form.cleaned_data['title'],
                                description=form.cleaned_data['description'],
                )
                message = 'Категория изменена'
            else:
                categorie = CategorieRecipe.objects.create(title=form.cleaned_data['title'],
                                            description=form.cleaned_data['description'],
                                            )
                message = 'Категория сохранена'
        context = {'title': 'Сайт рецептов',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   'message': message,
                   }
        return render(request, 'recipe/add_categorie.html', context)

class GetCategorieAll(View):
    def get(self, request):
        result = {}
        categorie_queryset = CategorieRecipe.objects.all()
        if categorie_queryset:
            result = categorie_queryset
        title_content = 'Список категорий:'
        context = {'title': 'Сайт рецептов',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'recipe/categorie_all.html', context)

class GetProduct(View):
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        product_id = kwargs.get('product_id',None)
        context = {'title': 'Сайт рецептов',}
        if product_id:
            product_select = Product.objects.get(pk=product_id)
            if product_select:
                form = AddEditProduct(initial={'name': product_select.name,
                                                'description': product_select.description,
                                                'add_date': product_select.add_date,
                                                 }
                                        )
                for key in form.fields.keys():
                    form.fields[key].disabled = True
                title_content = 'Просмотр информации по продукту'
                context['read'] = form
        else:
            title_content = 'Продукт не найден'
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_product.html', context)

class PostProduct(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ('recipe.view_product', 'recipe.change_product', 'recipe.add_product')
    login_url = settings.LOGIN_URL
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        product_id = kwargs.get('product_id',None)
        product_edit = kwargs.get('edit', None)
        context = {'title': 'Сайт рецептов',}
        if product_id:
            product_select = Product.objects.get(pk=product_id)
            if product_select:
                form = AddEditProduct(initial={'name': product_select.name,
                                                'description': product_select.description,
                                                'add_date': product_select.add_date,
                                                 }
                                        )
                if product_edit:
                    title_content = 'Редактирование информации о продукте'
                    context['form'] = form
        else:
            form = AddEditProduct()
            title_content = 'Добавление продукта'
            context['form'] = form
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_product.html', context)

    def post(self,request, **kwargs):
        form = AddEditProduct(request.POST)
        product_id = kwargs.get('product_id', None)
        product_edit = kwargs.get('edit', None)
        title_content = 'Добавление продукта'
        message = 'Продукт не сохранен'
        if form.is_valid():
            if product_id and product_edit:
                Product.objects.filter(pk=product_id).update(name=form.cleaned_data['name'],
                                description=form.cleaned_data['description'],
                )
                message = 'Продукт изменен'
            else:
                product = Product.objects.create(name=form.cleaned_data['name'],
                                            description=form.cleaned_data['description'],
                                            )
                message = 'Продукт сохранен'
        context = {'title': 'Сайт рецептов',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   'message': message,
                   }
        return render(request, 'recipe/add_product.html', context)

class GetProductAll(View):
    def get(self, request):
        result = {}
        product_queryset = Product.objects.all()
        if product_queryset:
            result = product_queryset
        title_content = 'Список продуктов:'
        context = {'title': 'Сайт рецептов',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'recipe/product_all.html', context)

class GetAuthor(View):
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        author_id = kwargs.get('author_id',None)
        context = {'title': 'Сайт рецептов',}
        if author_id:
            author_select = Author.objects.get(pk=author_id)
            if author_select:
                form = AddEditAuthor(initial={'name': author_select.name,
                                                'email': author_select.email,
                                                'registration_date': author_select.registration_date,
                                                 }
                                        )
                for key in form.fields.keys():
                    form.fields[key].disabled = True
                title_content = 'Просмотр информации по автору'
                context['read'] = form
        else:
            title_content = 'Автор не найден'
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_author.html', context)

class PostAuthor(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = ('recipe.view_author', 'recipe.change_author', 'recipe.add_author')
    login_url = settings.LOGIN_URL
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        author_id = kwargs.get('author_id',None)
        author_edit = kwargs.get('edit', None)
        context = {'title': 'Сайт рецептов',}
        if author_id:
            author_select = Author.objects.get(pk=author_id)
            if author_select:
                form = AddEditAuthor(initial={'name': author_select.name,
                                                'email': author_select.email,
                                                'registration_date': author_select.registration_date,
                                                 }
                                        )
                if author_edit:
                    title_content = 'Редактирование информации об авторе'
                    context['form'] = form
        else:
            form = AddEditAuthor()
            title_content = 'Добавление автора'
            context['form'] = form
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_author.html', context)

    def post(self,request, **kwargs):
        form = AddEditAuthor(request.POST)
        author_id = kwargs.get('author_id', None)
        author_edit = kwargs.get('edit', None)
        title_content = 'Добавление автора'
        message = 'Автор не сохранен'
        if form.is_valid():
            if author_id and author_edit:
                Author.objects.filter(pk=author_id).update(name=form.cleaned_data['name'],
                                email=form.cleaned_data['email'],
                )
                message = 'Автор изменен'
            else:
                author = Author.objects.create(name=form.cleaned_data['name'],
                                            email=form.cleaned_data['email'],
                                            )
                message = 'Автор сохранен'
        context = {'title': 'Сайт рецептов',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   'message': message,
                   }
        return render(request, 'recipe/add_author.html', context)

class GetAuthorAll(View):
    def get(self, request):
        result = {}
        author_queryset = Author.objects.all()
        if author_queryset:
            result = author_queryset
        title_content = 'Список авторов:'
        context = {'title': 'Сайт рецептов',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'recipe/author_all.html', context)

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

class GetReciepAll(View):
    def get(self, request):
        result = {}
        recipes_queryset = Recipe.objects.all()
        if recipes_queryset:
            for recipe in recipes_queryset:
                ingredients = recipe.ingredients.all()
                categories = recipe.categories.all()
                result[recipe] = {'ingredients': ingredients,
                                  'categories': categories}
        title_content = 'Список рецептов:'
        context = {'title': 'Сайт рецептов',
                    'content': {'title': title_content,
                                'result': result,
                                }
                    }
        return render(request, 'recipe/recipes_all.html', context)

class GetRecipe(View):
    def get(self,request, **kwargs):
        recipe_id = kwargs.get('recipe_id',None)
        context = {'title': 'Сайт рецептов',}
        if recipe_id:
            recipe_select = Recipe.objects.get(pk=recipe_id)
            if recipe_select:
                form = AddEditRecipe(initial={'name': recipe_select.name,
                                                 'description': recipe_select.description,
                                                 'ingredients': recipe_select.ingredients.all().values_list('id', flat=True),
                                                 'cooking_steps': recipe_select.cooking_steps,
                                                 'cooking_time': recipe_select.cooking_time,
                                                 'image': recipe_select.image,
                                                'author': recipe_select.author,
                                                'categories': recipe_select.categories.all().values_list('id', flat=True),
                                                'modify_date': recipe_select.modify_date,
                                                 }
                                        )
                for key in form.fields.keys():
                    form.fields[key].disabled = True
                title_content = 'Просмотр рецепта'
                context['read'] = form
        else:
            title_content = 'Рецепт не найден'
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_recipe.html', context)


class PostRecipe(LoginRequiredMixin, PermissionRequiredMixin, View):
    '''
    Добавление и редактирования рецепта. Требуется авторизация и наличие у пользователя разрешений
    '''
    permission_required = ('recipe.view_recipe', 'recipe.change_recipe', 'recipe.add_recipe')
    login_url = settings.LOGIN_URL
    def get(self,request, **kwargs):
        redirect_field_name = request.path
        recipe_id = kwargs.get('recipe_id',None)
        recipe_edit = kwargs.get('edit', None)
        context = {'title': 'Сайт рецептов',}
        if recipe_id:
            recipe_select = Recipe.objects.get(pk=recipe_id)
            if recipe_select:
                form = AddEditRecipe(initial={'name': recipe_select.name,
                                                 'description': recipe_select.description,
                                                 'ingredients': recipe_select.ingredients.all().values_list('id', flat=True),
                                                 'cooking_steps': recipe_select.cooking_steps,
                                                 'cooking_time': recipe_select.cooking_time,
                                                 'image': recipe_select.image,
                                                'author': recipe_select.author,
                                                'categories': recipe_select.categories.all().values_list('id', flat=True),
                                                'modify_date': recipe_select.modify_date,
                                                 }
                                        )
                if recipe_edit:
                    title_content = 'Редактирование рецепта'
                    context['form'] = form
                else:
                    for key in form.fields.keys():
                        form.fields[key].disabled = True
                    title_content = 'Просмотр рецепта'
                    context['read'] = form
        else:
            form = AddEditRecipe()
            title_content = 'Добавление рецепта'
            context['form'] = form
        context['content'] = {'title': title_content,
                               }
        return render(request, 'recipe/add_recipe.html', context)

    def post(self,request, **kwargs):
        redirect_field_name = request.path
        form = AddEditRecipe(request.POST, request.FILES)
        recipe_id = kwargs.get('recipe_id', None)
        recipe_edit = kwargs.get('edit', None)
        title_content = 'Добавление рецепта'
        message = 'Рецепт не сохранен'
        if form.is_valid():
            if recipe_id and recipe_edit:
                select_recipe = Recipe.objects.get(pk=recipe_id)
                if form.cleaned_data['image']:
                    image_update = form.cleaned_data['image']
                else:
                    image_update = select_recipe.image
                form.image = image_update
                Recipe.objects.filter(pk=recipe_id).update(name=form.cleaned_data['name'],
                                description=form.cleaned_data['description'],
                                cooking_steps=form.cleaned_data['cooking_steps'],
                                cooking_time=form.cleaned_data['cooking_time'],
                                author=form.cleaned_data['author'],
                                image=image_update,
                )
                select_recipe = Recipe.objects.get(pk=recipe_id)
                select_recipe.ingredients.set(form.cleaned_data['ingredients'])
                select_recipe.categories.set(form.cleaned_data['categories'])
                select_recipe.save()
                message = 'Рецепт изменен'
            else:
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
        context = {'title': 'Сайт рецептов',
                   'content': {'title': title_content,
                               },
                   'form': form,
                   'message': message,
                   }
        return render(request, 'recipe/add_recipe.html', context)
