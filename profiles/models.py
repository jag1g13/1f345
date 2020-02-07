from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User class as recommended by Django docs.

    See https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """