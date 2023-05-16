from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add your custom fields here, e.g.
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    serviceProvider = models.CharField(max_length=255, blank=True, null=True)
