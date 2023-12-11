from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from properties.use_cases.forms_use_cases import register_contract_use_case, register_house_use_case, register_payment_use_case


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
