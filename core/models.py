from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = PhoneNumberField()
    full_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username
