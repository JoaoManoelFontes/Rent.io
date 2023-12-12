from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from properties.use_cases.forms_use_cases import delete_contract_use_case, delete_expense_use_case, delete_payment_use_case, delete_property_use_case, register_apartment_use_case, register_building_use_case, register_contract_use_case, register_expense_use_case, register_house_use_case, register_payment_use_case


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
    if request.method == 'POST':
        register_apartment_use_case(request, building_id)
        return redirect('customer_home')
    return render(request, 'properties/apartment_form.html', {
        'title': 'Register Apartment | ' + request.user.username,
    })


@login_required(login_url='/login')
def contract_form(request, property_id, property_type):
    '''Contract form view.'''
    if request.method == 'POST':
        register_contract_use_case(request, property_id, property_type)
        return redirect('customer_home')
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
    if request.method == 'POST':
        register_expense_use_case(request, property_id, property_type)
        return redirect('customer_home')
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
    delete_expense_use_case(property_id, expense_id, property_type)
    return redirect('customer_home')


@login_required(login_url='/login')
def delete_contract(request, property_id, contract_id, property_type):
    '''Delete contract view.'''
    delete_contract_use_case(property_id, contract_id, property_type)
    return redirect('customer_home')