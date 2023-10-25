from django.shortcuts import get_object_or_404
from core.utils.get_buildings_infos import get_buildings_infos
from core.utils.validate_medias import validate_medias
from properties.models import Apartment, House, Building


def home_use_case():
    '''Properties listing use case.'''
    apartments = Apartment.objects.all()
    houses = House.objects.all()
    buildings = get_buildings_infos()

    context = {
        'title': 'Home',
        'apartments': apartments,
        'houses': houses,
        'buildings': buildings,
    }
    return context


def all_houses_use_case():
    '''Houses listing use case.'''
    houses = House.objects.all()
    context = {
        'title': 'Houses',
        'houses': houses,
    }
    return context


def all_buildings_use_case():
    '''Buildings listing use case.'''
    buildings = get_buildings_infos()
    context = {
        'title': 'Buildings',
        'buildings': buildings,
    }
    return context


def detail_building_use_case(pk):
    '''Building detail use case.'''
    building = get_object_or_404(Building, pk=pk)
    apartments = Apartment.objects.filter(building=building)
    has_many_medias = validate_medias(building)
    context = {
        'title': 'Building Detail | ' + building.name,
        'building': building,
        'apartments': apartments,
        'has_many_medias': has_many_medias,
    }
    return context


def detail_house_use_case(pk):
    '''House detail use case.'''
    house = get_object_or_404(House, pk=pk)
    has_many_medias = validate_medias(house)
    context = {
        'title': 'House Detail | ' + house.__str__(),
        'house': house,
        'has_many_medias': has_many_medias,
    }
    return context
