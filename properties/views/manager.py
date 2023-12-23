from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.use_cases.manager_use_cases import dashboard_use_case, detail_apartment_use_case, detail_building_use_case, detail_house_use_case, home_use_case


@login_required(login_url='/login')
def home(request):
    '''Home view for the properties managment.'''
    request.session['last_page'] = request.path
    return render(request, 'properties/home.html', context=home_use_case(request))


@login_required(login_url='/login')
def detail_building(request, building_id):
    '''Detail view for a building.'''
    request.session['last_page'] = request.path
    return render(request, 'properties/detail_building.html', context=detail_building_use_case(request, building_id))


@login_required(login_url='/login')
def detail_house(request, house_id):
    '''Detail view for a house.'''
    request.session['last_page'] = request.path
    return render(request, 'properties/detail_house.html', context=detail_house_use_case(request, house_id))


@login_required(login_url='/login')
def detail_apartment(request, apartment_id):
    '''Detail view for an apartment.'''
    request.session['last_page'] = request.path
    return render(request, 'properties/detail_apartment.html', context=detail_apartment_use_case(request, apartment_id))


@login_required(login_url='/login')
def dashboard(request, property_id, property_type):
    '''Dashboard view for the properties managment.'''
    request.session['last_page'] = request.path

    return render(request, 'properties/dashboard.html', context=dashboard_use_case(request, property_id, property_type))
