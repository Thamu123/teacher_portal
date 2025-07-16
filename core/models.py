from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class TeacherManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        teacher = self.model(email=email, name=name)
        teacher.set_password(password)  # Hash the password
        teacher.save()
        return teacher

class Teacher(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = TeacherManager()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    marks = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.name} - {self.subject}"
