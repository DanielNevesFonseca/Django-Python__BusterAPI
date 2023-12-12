from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(null=True, default=None)
    is_employee = models.BooleanField(
        ("employee status"),
        default=False,
        help_text=("Designates whether the user is an employee."),
    )
