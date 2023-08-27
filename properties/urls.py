from django.urls import path

from .views.manager import detail_building, detail_house, home

urlpatterns = [
    path('', home, name='customer_home'),
    path('building/<int:building_id>/', detail_building, name='building_detail'),
    path('house/<int:house_id>/', detail_house, name='house_detail'),
]
