from django.core.management.base import BaseCommand
from recipe.models import Author

class Command(BaseCommand):
    help = "Create Author"

    def handle(self, *args, **kwargs):
        tel_numbers = list(range(20))
        for i in range(1,11):
            author = Author(name=f'Author_{i}',
                            email=f'mail_author_{i}@mail.com',
                            )
            author.save()
            self.stdout.write(f'Create Author: {author}\n')