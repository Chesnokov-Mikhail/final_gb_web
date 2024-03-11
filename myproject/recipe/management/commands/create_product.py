from django.core.management.base import BaseCommand
from recipe.models import Product
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Product"

    def handle(self, *args, **kwargs):
        for i in range(1,101):
            product = Product(name = f'Product_{i}',
                                description = '. '.join(lorem_ipsum.paragraphs(1, common=False)),
                                )
            product.save()
            self.stdout.write(f'Create Product: {product}\n')