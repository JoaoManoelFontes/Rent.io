from django.urls import path

from .views.manager import detail_building, detail_house, home, house_payments_history, apartment_payments_history

urlpatterns = [
    path('', home, name='customer_home'),
    path('building/<int:building_id>/', detail_building, name='customer_building_detail'),
    path('house/<int:house_id>/', detail_house, name='customer_house_detail'),
    path('house_payments_history/<int:property_id>/', house_payments_history, name='house_payments_history'),
    path('apartment_payments_history/<int:property_id>/', apartment_payments_history, name='apartment_payments_history'),
]
