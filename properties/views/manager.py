from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import Apartment, Building, House

from properties.utils.properties_manager import get_late_payments_amount, get_occupied_properties_amount, get_properties_amount, get_properties_list


@login_required(login_url='/login')
def home(request):
    '''Home view for the properties managment.'''
    properties_amount = get_properties_amount(request.user)
    occupied_properties_amount = get_occupied_properties_amount(request.user)
    late_payments_amount = get_late_payments_amount(request.user)
    properties_list = get_properties_list(request.user)

    context = {
        'title': 'Home | ' + request.user.username,
        'properties_amount': properties_amount,
        'occupied_properties_amount': occupied_properties_amount,
        'late_payments_amount': late_payments_amount,
        'properties_list': properties_list,
    }

    return render(request, 'properties/home.html', context=context)


@login_required(login_url='/login')
def detail_building(request, building_id):
    '''Detail view for a building.'''
    building = Building.objects.get(id=building_id)

    context = {
        'title': 'Building Detail | ' + request.user.username,
        'building': building,
    }

    return render(request, 'properties/detail_building.html', context=context)


@login_required(login_url='/login')
def detail_house(request, house_id):
    '''Detail view for a house.'''
    house = House.objects.get(id=house_id)

    context = {
        'title': 'House Detail | ' + request.user.username,
        'house': house,
    }

    return render(request, 'properties/detail_house.html', context=context)


@login_required(login_url='/login')
def house_payments_history(request, property_id):
    '''Payments history view for a house.'''
    house = House.objects.get(id=property_id)
    payments = house.payment.all()
    context = {
        'title': 'Payments History | ' + house.__str__(),
        'payments': payments,
    }

    return render(request, 'properties/payments_history.html', context=context)


@login_required(login_url='/login')
def apartment_payments_history(request, property_id):
    '''Payments history view for an apartment.'''
    apartment = Apartment.objects.get(id=property_id)
    payments = apartment.payment.all()
    context = {
        'title': 'Payments History | ' + apartment.__str__(),
        'payments': payments,
    }

    return render(request, 'properties/payments_history.html', context=context)
