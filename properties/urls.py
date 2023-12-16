from django.urls import path

from .views.manager import detail_apartment, detail_building, detail_house, home
from .views.forms import apartment_form, building_form, contract_form, delete_expense, delete_payment, delete_property, expense_done, expense_form, house_form, payment_form, delete_contract, update_apartment, update_building, update_contract, update_expense, update_house, update_payment

urlpatterns = [
    path('', home, name='customer_home'),
    path('building/<int:building_id>/', detail_building, name='customer_building_detail'),
    path('house/<int:house_id>/', detail_house, name='customer_house_detail'),
    path('apartment/<int:apartment_id>/', detail_apartment, name='customer_apartment_detail'),
    path('register_house/', house_form , name='house_form'),
    path('register_building/', building_form , name='building_form'),
    path('register_apartment/<int:building_id>/', apartment_form , name='apartment_form'),
    path('register_contract/<int:property_id>/<str:property_type>/', contract_form , name='contract_form'),
    path('register_payment/<int:property_id>/<str:property_type>/', payment_form , name='payment_form'),
    path('register_expense/<int:property_id>/<str:property_type>/', expense_form , name='expense_form'),
    path('delete_property/<int:property_id>/<str:property_type>/', delete_property , name='delete_property'),
    path('delete_payment/<int:property_id>/<int:payment_id>/<str:property_type>/', delete_payment , name='delete_payment'),
    path('delete_expense/<int:property_id>/<int:expense_id>/<str:property_type>/', delete_expense , name='delete_expense'),
    path('delete_contract/<int:property_id>/<int:contract_id>/<str:property_type>/', delete_contract , name='delete_contract'),
    path('update_house/<int:house_id>/', update_house , name='update_house'),
    path('update_building/<int:building_id>/', update_building , name='update_building'),
    path('update_apartment/<int:apartment_id>/', update_apartment , name='update_apartment'),
    path('update_contract/<int:property_id>/<int:contract_id>/<str:property_type>/', update_contract , name='update_contract'),
    path('update_payment/<int:property_id>/<int:payment_id>/<str:property_type>/', update_payment , name='update_payment'),
    path('update_expense/<int:property_id>/<int:expense_id>/<str:property_type>/', update_expense , name='update_expense'),
    path('expense_done/<int:property_id>/<int:expense_id>/<str:property_type>/', expense_done , name='expense_done')
]
