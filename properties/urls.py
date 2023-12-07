from django.urls import path

from .views.manager import detail_apartment, detail_building, detail_house, home
from .views.forms import contract_form, house_form, payment_form

urlpatterns = [
    path('', home, name='customer_home'),
    path('building/<int:building_id>/', detail_building, name='customer_building_detail'),
    path('house/<int:house_id>/', detail_house, name='customer_house_detail'),
    path('apartment/<int:apartment_id>/', detail_apartment, name='customer_apartment_detail'),
    path('register_house/', house_form , name='house_form'),
    path('register_contract/<int:property_id>/', contract_form , name='contract_form'),
    path('register_payment/<int:property_id>/', payment_form , name='payment_form'),
]
