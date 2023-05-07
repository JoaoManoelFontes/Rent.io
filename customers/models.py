from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from cpf_field.models import CPFField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Customer(AbstractUser):
    instagram = models.URLField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    cpf = CPFField("cpf", unique=True)

    REQUIRED_FIELDS = ["email", "cpf", "password"]

    def __str__(self):
        return self.username


class CustomerManager(BaseUserManager):
    def create_user(self, username, email, cpf, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        if not cpf:
            raise ValueError("Users must have an cpf")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, cpf, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            cpf=cpf,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user
