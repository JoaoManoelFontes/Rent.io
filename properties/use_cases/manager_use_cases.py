from django.shortcuts import get_object_or_404
from properties.models import Apartment, Building, House
from properties.utils.properties_manager import get_house_infos, get_late_payments_amount, get_occupied_properties_amount, get_properties_amount, get_properties_list


def home_use_case(user):
    '''Properties managment use case.'''
    properties_amount = get_properties_amount(user)
    occupied_properties_amount = get_occupied_properties_amount(user)
    late_payments_amount = get_late_payments_amount(user)
    properties_list = get_properties_list(user)

    context = {
        'title': 'Home | ' + user.username,
        'properties_amount': properties_amount,
        'occupied_properties_amount': occupied_properties_amount,
        'late_payments_amount': late_payments_amount,
        'properties_list': properties_list,
    }

    return context


def detail_building_use_case(building_id):
    '''Building detail use case.'''
    building = get_object_or_404(Building, pk=building_id)
    apartments = Apartment.objects.filter(building=building)
    context = {
        'title': 'Building Detail | ' + building.name,
        'building': building,
        'apartments': apartments,
    }
    return context


def detail_house_use_case(house_id):
    '''House detail use case.'''
    house = get_house_infos(house_id)
    context = {
        'title': 'House Detail | ' + house.__str__(),
        'house': house,
    }
    return context


def house_payments_history_use_case(property_id):
    '''Payments history use case for a house.'''
    house = get_object_or_404(House, pk=property_id)
    payments = house.payment.all()
    context = {
        'title': 'Payments History | ' + house.__str__(),
        'payments': payments,
    }

    return context


def apartment_payments_history_use_case(property_id):
    '''Payments history use case for an apartment.'''
    apartment = get_object_or_404(Apartment, pk=property_id)
    payments = apartment.payment.all()
    context = {
        'title': 'Payments History | ' + apartment.__str__(),
        'payments': payments,
    }

    return context
