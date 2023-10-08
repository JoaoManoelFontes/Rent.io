from django.shortcuts import get_object_or_404
from properties.models import Apartment, House, Building


def home_use_case():
    '''Properties listing use case.'''
    apartments = Apartment.objects.all()
    houses = House.objects.all()
    buildings = Building.objects.all()
    for building in buildings:
        building.vacant = Apartment.objects.filter(vacant=True, building=building).count()
    context = {
        'title': 'Home',
        'apartments': apartments,
        'houses': houses,
        'buildings': buildings,
    }
    return context


def detail_building_use_case(pk):
    '''Building detail use case.'''
    building = get_object_or_404(Building, pk=pk)
    print(building)
    apartments = Apartment.objects.filter(building=building)
    context = {
        'title': 'Building Detail | ' + building.name,
        'building': building,
        'apartments': apartments,
    }
    return context


def detail_house_use_case(pk):
    '''House detail use case.'''
    house = get_object_or_404(House, pk=pk)
    context = {
        'title': 'House Detail | ' + house.__str__(),
        'house': house,
    }
    return context
