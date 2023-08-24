from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from properties.utils.properties_manager import get_late_payments_amount, get_occupied_properties_amount, get_properties_amount, get_properties_list


@login_required(login_url='/login')
def home(request):
    properties_amount = get_properties_amount(request.user)
    occupied_properties_amount = get_occupied_properties_amount(request.user)
    late_payments_amount = get_late_payments_amount(request.user)
    properties_list = get_properties_list(request.user)

    context = {
        'title': 'Home | ' + request.user.username,
        'properties_amount': properties_amount,
        'occupied_properties_amount': occupied_properties_amount,
        'late_payments_amount': late_payments_amount,
        'properties_list': properties_list,
    }

    return render(request, 'properties/home.html', context=context)
