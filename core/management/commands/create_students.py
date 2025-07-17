from django.core.management.base import BaseCommand
import random
from core.models import Student

class Command(BaseCommand):
    help = 'Create 20 dummy student records'

    def handle(self, *args, **kwargs):
        subjects = ['Math', 'Science', 'English', 'History', 'Physics']
        names = ['John', 'Alice', 'Bob', 'Diana', 'Ethan', 'Fiona', 'George', 'Hannah', 'Ian', 'Jane', 'Aarav Sharma', 'Isha Patel', 'Vihaan Mehta', 'Anaya Reddy', 'Arjun Nair', 'Meera Kapoor', 'Devansh Joshi', 'Sanya Verma', 'Ritvik', 'Yuvan']

        created = 0

        for i in range(20):
            name = random.choice(names)
            subject = random.choice(subjects)
            marks = random.randint(40, 100)

            student = Student.objects.filter(name__iexact=name, subject__iexact=subject).first()
            if student:
                student.marks += marks
                student.save()
            else:
                student = Student.objects.create(name=name, subject=subject, marks=marks)

            created += 1

        self.stdout.write(self.style.SUCCESS(f"Total {created} entries processed."))