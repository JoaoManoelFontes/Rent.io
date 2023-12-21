from django.urls import path
from .views.home import home, detail_building, detail_house, all_houses, all_buildings, about_us
from .views.auth import sign_in, sign_out, sign_up, edit_profile

urlpatterns = [
    path('', home, name='home'),
    path('building/<int:pk>/', detail_building, name='building_detail'),
    path('house/<int:pk>/', detail_house, name='house_detail'),
    path('login/', sign_in, name='sign_in'),
    path('signup/', sign_up, name='sign_up'),
    path('profile/', edit_profile, name='edit_profile'),
    path('logout/', sign_out, name='sign_out'),
    path('houses/', all_houses, name='all_houses'),
    path('buildings/', all_buildings, name='all_buildings'),
    path('about_us/', about_us, name='about_us'),
]
