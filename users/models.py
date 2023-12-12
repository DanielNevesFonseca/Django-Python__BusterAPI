from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(null=True, default=None)
    is_employee = models.BooleanField(
        ("employee status"),
        default=False,
        help_text=("Designates whether the user is an employee."),
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, max_length=127, unique=True)
