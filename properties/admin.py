from django.contrib import admin
from .models import House, Building, Apartment, Payment, Expense, Contract, Media

# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'base_price', 'late_payment', 'vacant')


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city')


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'rooms', 'building', 'late_payment', 'vacant')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('date', 'base_payment_month', 'value')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    '''Admin View for Expense'''

    list_display = ('value', 'description', 'done')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    '''Admin View for Contract'''

    list_display = ('base_payment_date', 'due_date', 'price', 'content_object', 'tenant_name', 'tenant_phone')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    '''Admin View for Media'''

    list_display = ('content_type', 'content_object')
