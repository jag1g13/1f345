from django.contrib.auth.models import AbstractUser
from django.db import models

from constance import settings


class User(AbstractUser):
    """
    Custom User class as recommended by Django docs.

    See https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """

    #: User's prefered units of time measurement
    time_units = models.CharField(max_length=15,
                                  blank=True, null=True)

    def get_time_units(self) -> str:
        """
        Get the time units used by this user.
        """
        return self.time_units or settings.DEFAULT_TIME_UNIT
