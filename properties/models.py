from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from rent_io import settings
from .utils.model_managers import GenericModelManager
from phonenumber_field.modelfields import PhoneNumberField


class Media(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = GenericModelManager()

    def __str__(self) -> str:
        return self.content_object.__str__()


class Expense(models.Model):
    description = models.TextField()
    done = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    objects = GenericModelManager()

    def __str__(self):
        return "Despesa de " + self.content_object.__str__()


class Payment(models.Model):
    date = models.DateField()
    base_payment_month = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    objects = GenericModelManager()

    def __str__(self):
        return "Histórico de " + self.content_object.__str__()


class Contract(models.Model):
    contract_file = models.FileField(upload_to="contracts/", null=True, blank=True)
    base_payment_date = models.DateField()
    tenant_name = models.CharField(max_length=100)
    tenant_phone = PhoneNumberField(null=True, blank=True)
    due_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    objects = GenericModelManager()

    def __str__(self):
        return "Contrato de " + self.content_object.__str__()


class Property(models.Model):
    class Meta:
        abstract = True

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    description = models.TextField()

    media = GenericRelation(Media)
    expenses = GenericRelation(Expense)


class House(Property):
    garage = models.BooleanField(default=False)
    backyard = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    suites = models.IntegerField()
    area = models.IntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    vacant = models.BooleanField(default=True)
    late_payment = models.BooleanField(default=False)

    contract = GenericRelation(Contract)
    payment = GenericRelation(Payment)
    expenses = GenericRelation(Expense)

    def __str__(self):
        return "Casa em " + self.city


class Building(Property):
    name = models.CharField(max_length=50)
    recreation_area = models.BooleanField()
    elevator = models.BooleanField(default=False)
    concierge = models.BooleanField(default=False)
    floors = models.IntegerField()

    def __str__(self):
        return "Prédio " + self.name + " em " + self.city


class Apartment(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    suites = models.IntegerField()
    area = models.IntegerField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    vacant = models.BooleanField(default=True)
    late_payment = models.BooleanField(default=False)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    payment = GenericRelation(Payment)
    contract = GenericRelation(Contract)
    expenses = GenericRelation(Expense)

    def __str__(self):
        return "Apartamento " + str(self.number) + " - " + self.building.name
