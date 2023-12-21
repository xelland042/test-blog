from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from post.models import Tag


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['filename'][0], 'r') as file:
            content = file.readlines()
            # print(content)
            for tag in content:
                Tag.objects.create(name=tag, slug=slugify(tag))

        self.stdout.write(
            self.style.SUCCESS("Successfully created")
        )
