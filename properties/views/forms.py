from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from properties.use_cases.forms_use_cases import register_contract_use_case, register_house_use_case


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
def contract_form(request, house_id):
    '''Contract form view.'''
    if request.method == 'POST':
        register_contract_use_case(request, house_id)
        return redirect('customer_home')
    return render(request, 'properties/contract_form.html', {
        'title': 'Register Contract | ' + request.user.username,
    })
