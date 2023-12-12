from ..models import Apartment, Building, House


def register_house_use_case(request):
    '''register house use case.'''
    house = House.objects.create(
        customer=request.user,
        address=request.POST.get('address'),
        city=request.POST.get('city'),
        description=request.POST.get('description'),
        garage=True if request.POST.get('garage') == 'on' else False,
        backyard=True if request.POST.get('backyard') == 'on' else False,
        pool=True if request.POST.get('pool') == 'on' else False,
        rooms=request.POST.get('rooms'),
        bathrooms=request.POST.get('bathrooms'),
        suites=request.POST.get('suites'),
        area=request.POST.get('area'),
        base_price=request.POST.get('base_price'),
    )

    house.media.create(
        image=request.FILES.get('image'),
    )

    house.media.create(
        image=request.FILES.get('image2'),
    )

    house.save()


def register_building_use_case(request):
    '''register building use case.'''
    building = Building.objects.create(
        customer=request.user,
        address=request.POST.get('address'),
        city=request.POST.get('city'),
        description=request.POST.get('description'),
        name=request.POST.get('name'),
        recreation_area=True if request.POST.get('recreation_area') == 'on' else False,
        elevator=True if request.POST.get('elevator') == 'on' else False,
        concierge=True if request.POST.get('concierge') == 'on' else False,
        floors=request.POST.get('floors'),
    )

    building.media.create(
        image=request.FILES.get('image'),
    )

    building.media.create(
        image=request.FILES.get('image2'),
    )

    building.save()


def register_apartment_use_case(request, building_id):
    '''register apartment use case.'''
    building = Building.objects.get(id=building_id)

    apartment = Apartment.objects.create(
        floor=request.POST.get('floor'),
        number=request.POST.get('number'),
        rooms=request.POST.get('rooms'),
        bathrooms=request.POST.get('bathrooms'),
        suites=request.POST.get('suites'),
        area=request.POST.get('area'),
        base_price=request.POST.get('base_price'),
        building=building,
    )

    apartment.save()


def register_contract_use_case(request, property_id, property_type):
    '''register contract use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    property_object.contract.create(
        contract_file=request.FILES.get('contract_file'),
        base_payment_date=request.POST.get('base_payment_date'),
        due_date=request.POST.get('due_date'),
        price=request.POST.get('price')
    )

    property_object.vacant = False

    property_object.save()


def register_payment_use_case(request, property_id, property_type):
    '''register payment use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    property_object.payment.create(
        date=request.POST.get('date'),
        base_payment_month=request.POST.get('base_payment_month'),
        value=request.POST.get('value'),
    )

    property_object.save()


def register_expense_use_case(request, property_id, property_type):
    '''register expense use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    property_object.expenses.create(
        description=request.POST.get('description'),
        done=True if request.POST.get('done') == 'on' else False,
        value=request.POST.get('value'),
    )

    property_object.save()


def delete_property_use_case(property_id, property_type):
    '''delete property use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    elif property_type == 'apartment':
        property_object = Apartment.objects.get(id=property_id)
    elif property_type == 'building':
        property_object = Building.objects.get(id=property_id)

    property_object.delete()


def delete_payment_use_case(property_id, payment_id, property_type):
    '''delete payment use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    payment_object = property_object.payment.get(id=payment_id)
    payment_object.delete()


def delete_expense_use_case(property_id, expense_id, property_type):
    '''delete expense use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Building.objects.get(id=property_id)

    expense_object = property_object.expenses.get(id=expense_id)
    expense_object.delete()


def delete_contract_use_case(property_id, contract_id, property_type):
    '''delete contract use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    contract_object = property_object.contract.get(id=contract_id)
    contract_object.delete()
    property_object.payment.all().delete()
    property_object.vacant = True
    property_object.save()
