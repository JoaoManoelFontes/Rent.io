from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instagram = models.URLField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    cpf = CPFField("cpf", unique=True)

    def __str__(self):
        return self.username
