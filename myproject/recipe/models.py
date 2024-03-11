from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    registration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Author: {self.name}, email: {self.email}, registration_date: {self.registration_date}'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default=None)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Productname: {self.name}'

class CategorieRecipe(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'Categoriename: {self.title}'

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default=None)
    ingredients = models.ManyToManyField(to=Product)
    cooking_steps = models.TextField(default=None)
    cooking_time = models.TimeField()
    image = models.ImageField(null=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=CategorieRecipe)

    def __str__(self):
        ingredients = [product.name for product in self.ingredients.all()]
        categories = [categorie.title for categorie in self.categories.all()]
        return f'Recipename: {self.name}, description: {self.description}, author: {self.author},' \
               f' ingredients: {ingredients}, categories: {categories}'