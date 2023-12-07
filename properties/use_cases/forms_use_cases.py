from ..models import Apartment, House


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

    house.save()


def register_contract_use_case(request, property_id):
    '''register contract use case.'''
    if isinstance(property_id, House):
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


def register_payment_use_case(request, property_id):
    '''register payment use case.'''
    if isinstance(property_id, House):
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    property_object.payment.create(
        date=request.POST.get('date'),
        base_payment_month=request.POST.get('base_payment_month'),
        value=request.POST.get('value'),
    )

    property_object.save()
