from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from properties.models import Apartment, Building, House

from properties.use_cases.forms_use_cases import delete_contract_use_case, delete_expense_use_case, delete_payment_use_case, delete_property_use_case, make_expense_done_use_case, register_apartment_use_case, register_building_use_case, register_contract_use_case, register_expense_use_case, register_house_use_case, register_payment_use_case, update_apartment_use_case, update_building_use_case, update_contract_use_case, update_expense_use_case, update_house_use_case, update_payment_use_case


@login_required(login_url='/login')
def house_form(request):
    '''House form view.'''
    if request.method == 'POST':
        register_house_use_case(request)
        return redirect('customer_home')
    return render(request, 'properties/house_form.html', {
        'title': 'Register House | ' + request.user.username,
    })


@login_required(login_url='/login')
def building_form(request):
    '''Building form view.'''
    if request.method == 'POST':
        register_building_use_case(request)
        return redirect('customer_home')
    return render(request, 'properties/building_form.html', {
        'title': 'Register Building | ' + request.user.username,
    })


@login_required(login_url='/login')
def apartment_form(request, building_id):
    '''Apartment form view.'''
    last_page = request.session.get('last_page', '/')
    if request.method == 'POST':
        register_apartment_use_case(request, building_id)
        return redirect(last_page)
    return render(request, 'properties/apartment_form.html', {
        'title': 'Register Apartment | ' + request.user.username,
    })


@login_required(login_url='/login')
def contract_form(request, property_id, property_type):
    '''Contract form view.'''
    last_page = request.session.get('last_page', '/')
    if request.method == 'POST':
        register_contract_use_case(request, property_id, property_type)
        return redirect(last_page)
    return render(request, 'properties/contract_form.html', {
        'title': 'Register Contract | ' + request.user.username,
    })


@login_required(login_url='/login')
def payment_form(request, property_id, property_type):
    '''Payment form view.'''
    if request.method == 'POST':
        register_payment_use_case(request, property_id, property_type)
        return redirect('customer_home')
    return render(request, 'properties/payment_form.html', {
        'title': 'Register Payment | ' + request.user.username,
    })


@login_required(login_url='/login')
def expense_form(request, property_id, property_type):
    '''Expense form view.'''
    last_page = request.session.get('last_page', '/')
    if request.method == 'POST':
        register_expense_use_case(request, property_id, property_type)
        return redirect(last_page)
    return render(request, 'properties/expense_form.html', {
        'title': 'Register Expense | ' + request.user.username,
    })


@login_required(login_url='/login')
def delete_property(request, property_id, property_type):
    '''Delete property view.'''
    delete_property_use_case(property_id, property_type)
    return redirect('customer_home')


@login_required(login_url='/login')
def delete_payment(request, property_id, payment_id, property_type):
    '''Delete payment view.'''
    delete_payment_use_case(property_id, payment_id, property_type)
    return redirect('customer_home')


@login_required(login_url='/login')
def delete_expense(request, property_id, expense_id, property_type):
    '''Delete expense view.'''
    last_page = request.session.get('last_page', '/')
    delete_expense_use_case(property_id, expense_id, property_type)
    return redirect(last_page)


@login_required(login_url='/login')
def delete_contract(request, property_id, contract_id, property_type):
    '''Delete contract view.'''
    last_page = request.session.get('last_page', '/')
    delete_contract_use_case(property_id, contract_id, property_type)
    return redirect(last_page)


@login_required(login_url='/login')
def update_house(request, house_id):
    '''Update house view.'''
    last_page = request.session.get('last_page', '/')
    if request.method == 'POST':
        update_house_use_case(request, house_id)
        return redirect(last_page)

    house = House.objects.get(id=house_id)
    return render(request, 'properties/house_form.html', {
        'title': 'Update House | ' + request.user.username, 'house': house
    })


@login_required(login_url='/login')
def update_building(request, building_id):
    '''Update building view.'''
    last_page = request.session.get('last_page', '/')

    if request.method == 'POST':
        update_building_use_case(request, building_id)
        return redirect(last_page)

    building = Building.objects.get(id=building_id)
    return render(request, 'properties/building_form.html', {
        'title': 'Update Building | ' + request.user.username, 'building': building
    })


@login_required(login_url='/login')
def update_apartment(request, apartment_id):
    '''Update apartment view.'''
    last_page = request.session.get('last_page', '/')

    if request.method == 'POST':
        update_apartment_use_case(request, apartment_id)
        return redirect(last_page)

    apartment = Apartment.objects.get(id=apartment_id)
    return render(request, 'properties/apartment_form.html', {
        'title': 'Update Apartment | ' + request.user.username, 'apartment': apartment
    })


@login_required(login_url='/login')
def update_contract(request, property_id, contract_id, property_type):
    '''Update contract view.'''
    last_page = request.session.get('last_page', '/')
    if request.method == 'POST':
        update_contract_use_case(request, property_id, contract_id, property_type)
        return redirect(last_page)

    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    contract_object = property_object.contract.get(id=contract_id)
    return render(request, 'properties/contract_form.html', {
        'title': 'Update Contract | ' + request.user.username, 'contract': contract_object
    })


@login_required(login_url='/login')
def update_payment(request, property_id, payment_id, property_type):
    '''Update payment view.'''
    if request.method == 'POST':
        update_payment_use_case(request, property_id, payment_id, property_type)
        return redirect('customer_home')

    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Apartment.objects.get(id=property_id)

    payment_object = property_object.payment.get(id=payment_id)
    return render(request, 'properties/payment_form.html', {
        'title': 'Update Payment | ' + request.user.username, 'payment': payment_object
    })


@login_required(login_url='/login')
def update_expense(request, property_id, expense_id, property_type):
    '''Update expense view.'''
    last_page = request.session.get('last_page', '/')

    if request.method == 'POST':
        update_expense_use_case(request, property_id, expense_id, property_type)
        return redirect(last_page)

    if property_type == 'house':
        property_object = House.objects.get(id=property_id)
    else:
        property_object = Building.objects.get(id=property_id)

    expense_object = property_object.expenses.get(id=expense_id)
    return render(request, 'properties/expense_form.html', {
        'title': 'Update Expense | ' + request.user.username, 'expense': expense_object
    })


@login_required(login_url='/login')
def expense_done(request, property_id, expense_id, property_type):
    '''Done expense view.'''
    last_page = request.session.get('last_page', '/')
    make_expense_done_use_case(property_id, expense_id, property_type)
    return redirect(last_page)
