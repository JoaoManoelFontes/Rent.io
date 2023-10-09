from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.use_cases.home_use_cases import detail_house_use_case
from properties.use_cases.manager_use_cases import apartment_payments_history_use_case, detail_building_use_case, home_use_case, house_payments_history_use_case


@login_required(login_url='/login')
def home(request):
    '''Home view for the properties managment.'''
    return render(request, 'properties/home.html', context=home_use_case(request.user))


@login_required(login_url='/login')
def detail_building(request, building_id):
    '''Detail view for a building.'''
    return render(request, 'properties/detail_building.html', context=detail_building_use_case(building_id))


@login_required(login_url='/login')
def detail_house(request, house_id):
    '''Detail view for a house.'''
    return render(request, 'properties/detail_house.html', context=detail_house_use_case(house_id))


@login_required(login_url='/login')
def house_payments_history(request, property_id):
    '''Payments history view for a house.'''
    return render(request, 'properties/payments_history.html', context=house_payments_history_use_case(property_id))


@login_required(login_url='/login')
def apartment_payments_history(request, property_id):
    '''Payments history view for an apartment.'''
    return render(request, 'properties/payments_history.html', context=apartment_payments_history_use_case(property_id))
