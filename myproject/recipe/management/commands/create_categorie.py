from django.core.management.base import BaseCommand
from recipe.models import CategorieRecipe
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Categorie recipe"

    def handle(self, *args, **kwargs):
        for i in range(1,10):
            categorie = CategorieRecipe(name = f'CategorieRecipe_{i}',
                                description = '. '.join(lorem_ipsum.words(4,common=False)),
                                )
            categorie.save()
            self.stdout.write(f'Create Categorie recipe: {categorie}\n')