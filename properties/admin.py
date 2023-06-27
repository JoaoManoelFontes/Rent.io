from django.contrib import admin
from .models import House, Building, Apartment, Payment, Expense, Contract

# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'base_price', 'late_payment', 'vacant')


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')


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

    list_display = ('contract_file', 'base_payment_date', 'due_date', 'price', 'content_object')
