from django.urls import path
from .views.home import home, detail_building, detail_house, all_houses, all_buildings, about_us
from .views.auth import sign_in, sign_out, sign_up

urlpatterns = [
    path('', home, name='home'),
    path('building/<int:pk>/', detail_building, name='building_detail'),
    path('house/<int:pk>/', detail_house, name='house_detail'),
    path('login/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', sign_out, name='sign_out'),
    path('all_houses/', all_houses, name='all_houses'),
    path('all_buildings/', all_buildings, name='all_buildings'),
    path('about_us/', about_us, name='about_us'),
]
