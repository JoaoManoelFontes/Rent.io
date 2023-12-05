from ..models import House


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


def register_contract_use_case(request, house_id):
    '''register contract use case.'''
    house = House.objects.get(id=house_id)
    house.contract.create(
        contract_file=request.FILES.get('contract_file'),
        base_payment_date=request.POST.get('base_payment_date'),
        due_date=request.POST.get('due_date'),
        price=request.POST.get('price')
    )

    house.vacant = False

    house.save()
