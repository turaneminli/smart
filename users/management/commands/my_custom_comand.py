from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "A description of the comand"

    def handle(self, *args, **options):
        self.stdout.write("My sample command just run")
        