from django.db import models
from django.contrib.auth.models import AbstractUser
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField


class Customer(AbstractUser):
    instagram = models.URLField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    cpf = CPFField("cpf", unique=True)

    def __str__(self):
        return self.username
