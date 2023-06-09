from django.contrib.auth.models import AbstractUser
# from django.utils.crypto import get_random_string
from django.db import models


class CustomUser(AbstractUser):
    # Add your custom fields here, e.g.
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    service_provider = models.CharField(max_length=255, blank=True, null=True)
