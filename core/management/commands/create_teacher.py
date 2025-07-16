from django.core.management.base import BaseCommand
from core.models import Teacher
from getpass import getpass  # for secure password input

class Command(BaseCommand):
    help = "Create a teacher user interactively"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Create a new Teacher\n"))

        email = input("Email: ").strip()
        name = input("Name: ").strip()
        password = getpass("Password: ")

        if Teacher.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR("A teacher with this email already exists."))
            return

        teacher = Teacher.objects.create_user(email=email, name=name, password=password)
        self.stdout.write(self.style.SUCCESS(f"Teacher '{teacher.name}' created successfully!"))
