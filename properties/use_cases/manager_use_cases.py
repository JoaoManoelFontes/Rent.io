from properties.utils.properties_manager import get_apartment_infos, get_apartment_list, get_building_infos, get_house_infos, get_late_payments_amount, get_occupied_properties_amount, get_properties_amount, get_properties_list


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
    building = get_building_infos(building_id)
    apartments = get_apartment_list(building_id)
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


def detail_apartment_use_case(apartment_id):
    '''Apartment detail use case.'''
    apartment = get_apartment_infos(apartment_id)
    context = {
        'title': 'Apartment Detail | ' + apartment.__str__(),
        'apartment': apartment,
    }
    return context
