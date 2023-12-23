from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField(null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="customers/", null=True, blank=True)

    def __str__(self):
        return self.username
