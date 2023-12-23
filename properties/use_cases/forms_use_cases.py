from ..models import Apartment, Building, House


def register_house_use_case(request):
    '''register house use case.'''
    house = House.objects.create(
        customer=request.user,
        street=request.POST.get('street'),
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

    if request.FILES.get('image') is not None:
        house.media.create(
            image=request.FILES.get('image'),
        )

    if request.FILES.get('image2') is not None:
        house.media.create(
            image=request.FILES.get('image2'),
        )
    house.save()


def register_building_use_case(request):
    '''register building use case.'''
    building = Building.objects.create(
        customer=request.user,
        street=request.POST.get('street'),
        city=request.POST.get('city'),
        description=request.POST.get('description'),
        name=request.POST.get('name'),
        recreation_area=True if request.POST.get('recreation_area') == 'on' else False,
        elevator=True if request.POST.get('elevator') == 'on' else False,
        concierge=True if request.POST.get('concierge') == 'on' else False,
        floors=request.POST.get('floors'),
    )

    if request.FILES.get('image') is not None:
        building.media.create(
            image=request.FILES.get('image'),
        )

    if request.FILES.get('image2') is not None:
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
        price=request.POST.get('price'),
        tenant_name=request.POST.get('tenant_name'),
        tenant_phone=request.POST.get('tenant_phone') if request.POST.get('tenant_phone') else None,
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
        property_object = Building.objects.get(id=property_id)

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
        property_object.media.all().delete()
        property_object.payment.all().delete()
        property_object.contract.all().delete()
        property_object.expenses.all().delete()
        property_object.media.all().delete()
    elif property_type == 'apartment':
        property_object = Apartment.objects.get(id=property_id)
        property_object.payment.all().delete()
        property_object.contract.all().delete()
    elif property_type == 'building':
        property_object = Building.objects.get(id=property_id)
        property_object.media.all().delete()
        property_object.expenses.all().delete()
        property_object.media.all().delete()
        apartments = Apartment.objects.filter(building=property_object)
        apartments.delete()

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


def update_house_use_case(request, house_id):
    '''update house use case.'''
    house = House.objects.get(id=house_id)

    house.street = request.POST.get('street') if request.POST.get('street') else house.street
    house.city = request.POST.get('city') if request.POST.get('city') else house.city
    house.description = request.POST.get('description') if request.POST.get('description') else house.description
    house.garage = True if request.POST.get('garage') == 'on' else False
    house.backyard = True if request.POST.get('backyard') == 'on' else False
    house.pool = True if request.POST.get('pool') == 'on' else False
    house.rooms = request.POST.get('rooms') if request.POST.get('rooms') else house.rooms
    house.bathrooms = request.POST.get('bathrooms') if request.POST.get('bathrooms') else house.bathrooms
    house.suites = request.POST.get('suites') if request.POST.get('suites') else house.suites
    house.area = request.POST.get('area') if request.POST.get('area') else house.area
    house.base_price = request.POST.get('base_price') if request.POST.get('base_price') else house.base_price
    if request.FILES.get('image') is not None:
        house.media.all()[0].delete()
        house.media.create(
            image=request.FILES.get('image'),
        )
    if request.FILES.get('image2') is not None:
        if house.media.all().count() > 1:
            house.media.all()[1].delete()
        house.media.create(
            image=request.FILES.get('image2'),
        )

    house.save()


def update_building_use_case(request, building_id):
    '''update building use case.'''
    building = Building.objects.get(id=building_id)

    building.street = request.POST.get('street') if request.POST.get('street') else building.street
    building.city = request.POST.get('city') if request.POST.get('city') else building.city
    building.description = request.POST.get('description') if request.POST.get('description') else building.description
    building.name = request.POST.get('name') if request.POST.get('name') else building.name
    building.recreation_area = True if request.POST.get('recreation_area') == 'on' else False
    building.elevator = True if request.POST.get('elevator') == 'on' else False
    building.concierge = True if request.POST.get('concierge') == 'on' else False
    building.floors = request.POST.get('floors') if request.POST.get('floors') else building.floors

    if request.FILES.get('image') is not None:
        building.media.all()[0].delete()
        building.media.create(
            image=request.FILES.get('image'),
        )

    if request.FILES.get('image2') is not None:
        if building.media.all().count() > 1:
            building.media.all()[1].delete()
        building.media.create(
            image=request.FILES.get('image2'),
        )

    building.save()


def update_apartment_use_case(request, building_id):
    '''update apartment use case.'''
    apartment = Apartment.objects.get(id=building_id)

    apartment.floor = request.POST.get('floor') if request.POST.get('floor') else apartment.floor
    apartment.number = request.POST.get('number') if request.POST.get('number') else apartment.number
    apartment.rooms = request.POST.get('rooms') if request.POST.get('rooms') else apartment.rooms
    apartment.bathrooms = request.POST.get('bathrooms') if request.POST.get('bathrooms') else apartment.bathrooms
    apartment.suites = request.POST.get('suites') if request.POST.get('suites') else apartment.suites
    apartment.area = request.POST.get('area') if request.POST.get('area') else apartment.area
    apartment.base_price = request.POST.get('base_price') if request.POST.get('base_price') else apartment.base_price

    apartment.save()


def update_contract_use_case(request, property_id, contract_id, property_type):
    '''update contract use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    contract_object = property_object.contract.get(id=contract_id)

    contract_object.contract_file = request.FILES.get('contract_file') if request.FILES.get('contract_file') else contract_object.contract_file
    contract_object.base_payment_date = request.POST.get('base_payment_date') if request.POST.get('base_payment_date') else contract_object.base_payment_date
    contract_object.due_date = request.POST.get('due_date') if request.POST.get('due_date') else contract_object.due_date
    contract_object.price = request.POST.get('price') if request.POST.get('price') else contract_object.price
    contract_object.tenant_name = request.POST.get('tenant_name') if request.POST.get('tenant_name') else contract_object.tenant_name
    contract_object.tenant_phone = request.POST.get('tenant_phone') if request.POST.get('tenant_phone') else contract_object.tenant_phone

    contract_object.save()


def update_payment_use_case(request, property_id, payment_id, property_type):
    '''update payment use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    payment_object = property_object.payment.get(id=payment_id)

    payment_object.date = request.POST.get('date') if request.POST.get('date') else payment_object.date
    payment_object.base_payment_month = request.POST.get('base_payment_month') if request.POST.get('base_payment_month') else payment_object.base_payment_month
    payment_object.value = request.POST.get('value') if request.POST.get('value') else payment_object.value

    payment_object.save()


def update_expense_use_case(request, property_id, expense_id, property_type):
    '''update expense use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Building.objects.get(id=property_id)

    expense_object = property_object.expenses.get(id=expense_id)

    expense_object.description = request.POST.get('description') if request.POST.get('description') else expense_object.description
    expense_object.done = True if request.POST.get('done') == 'on' else False
    expense_object.value = request.POST.get('value') if request.POST.get('value') else expense_object.value

    expense_object.save()


def make_expense_done_use_case(property_id, expense_id, property_type):
    '''make expense done use case.'''
    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Building.objects.get(id=property_id)

    expense_object = property_object.expenses.get(id=expense_id)

    expense_object.done = True
    expense_object.save()
