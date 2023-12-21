from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import json

User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open(options['filename'][0], 'r') as file:
            data = json.load(file)
            for user in data:
                User.objects.create(username=user['username'],
                                    email=user['email'],
                                    password=user['password'], is_staff=True)

        self.stdout.write(
            self.style.SUCCESS("Successfully created")
        )
