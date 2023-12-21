from django.core.management.base import BaseCommand
from post.models import Post, Tag
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['filename'][0], 'r') as file:
            data = json.load(file)
            for post in data:
                tags = post['tags']
                post = Post.objects.create(title=post['title'], content=post['content'],
                                           image=f"images/{post['image']}")
                post.save()
                tags = Tag.objects.filter(id__in=tags)
                post.tags.add(*tags)
                post.save()

        self.stdout.write(
            self.style.SUCCESS("Successfully created")
        )
