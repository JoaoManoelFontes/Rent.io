from properties.utils.properties_manager import get_apartment_infos, get_apartment_list, get_building_infos, get_house_infos, get_late_payments_amount, get_occupied_properties_amount, get_properties_amount, get_properties_list
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_use_case(request):
    '''Properties managment use case.'''
    properties_amount = get_properties_amount(request.user)
    occupied_properties_amount = get_occupied_properties_amount(request.user)
    late_payments_amount = get_late_payments_amount(request.user)
    properties_list = get_properties_list(request.user)

    paginator = Paginator(properties_list, 5)
    page = request.GET.get('page')
    try:
        properties_list = paginator.page(page)
    except PageNotAnInteger:
        properties_list = paginator.page(1)
    except EmptyPage:
        properties_list = paginator.page(paginator.num_pages)

    context = {
        'title': 'Home | ' + request.user.username,
        'properties_amount': properties_amount,
        'occupied_properties_amount': occupied_properties_amount,
        'late_payments_amount': late_payments_amount,
        'properties_list': properties_list,
    }

    return context


def detail_building_use_case(request, building_id):
    '''Building detail use case.'''
    building = get_building_infos(building_id)
    apartments = get_apartment_list(building_id)

    paginator = Paginator(apartments, 5)
    page = request.GET.get('page')
    try:
        apartments = paginator.page(page)
    except PageNotAnInteger:
        apartments = paginator.page(1)
    except EmptyPage:
        apartments = paginator.page(paginator.num_pages)

    context = {
        'title': 'Building Detail | ' + building.name,
        'building': building,
        'apartments': apartments,
    }
    return context


def detail_house_use_case(request, house_id):
    '''House detail use case.'''
    house = get_house_infos(house_id)

    context = {
        'title': 'House Detail | ' + house.__str__(),
        'house': house,
    }

    if len(house.payment.all()) > 0:
        paginator = Paginator(house.payments, 5)
        page = request.GET.get('page')

        try:
            house.payments = paginator.page(page)
        except PageNotAnInteger:
            house.payments = paginator.page(1)
        except EmptyPage:
            house.payments = paginator.page(paginator.num_pages)

        context['payment'] = house.payments

    return context


def detail_apartment_use_case(request, apartment_id):
    '''Apartment detail use case.'''
    apartment = get_apartment_infos(apartment_id)

    paginator = Paginator(apartment.payments, 5)
    page = request.GET.get('page')

    try:
        apartment.payments = paginator.page(page)
    except PageNotAnInteger:
        apartment.payments = paginator.page(1)
    except EmptyPage:
        apartment.payments = paginator.page(paginator.num_pages)

    context = {
        'title': 'Apartment Detail | ' + apartment.__str__(),
        'apartment': apartment,
        'payment': apartment.payments,
    }
    return context


def dashboard_use_case(request, property_id, property_type):
    '''Dashboard use case.'''
    if property_type == 'building':
        property = get_building_infos(property_id)
    elif property_type == 'house':
        property = get_house_infos(property_id)

    context = {
        'title': 'Dashboard | ' + request.user.username,
        'property': property,
    }
    return context
