from django.urls import path

from .views.manager import detail_apartment, detail_building, detail_house, home

urlpatterns = [
    path('', home, name='customer_home'),
    path('building/<int:building_id>/', detail_building, name='customer_building_detail'),
    path('house/<int:house_id>/', detail_house, name='customer_house_detail'),
    path('apartment/<int:apartment_id>/', detail_apartment, name='customer_apartment_detail')
]
