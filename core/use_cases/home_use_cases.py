from django.shortcuts import get_object_or_404
from core.utils.filter import house_filter
from core.utils.get_all_buildings_infos import get_all_buildings_infos, get_home_buildings_info
from core.utils.validate_medias import validate_medias
from properties.models import Apartment, House, Building


def home_use_case():
    '''Properties listing use case.'''
    houses = House.objects.all()
    buildings = get_home_buildings_info()

    context = {
        'title': 'Home',
        'houses': houses,
        'buildings': buildings,
    }
    return context


def all_houses_use_case(request):
    '''Houses listing use case.'''
    property = House.objects.filter(vacant=True)

    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    garage = request.GET.get("garage") if request.GET.get("garage") is not None else ""
    pool = request.GET.get("pool") if request.GET.get("pool") is not None else ""
    backyard = request.GET.get("backyard") if request.GET.get("backyard") is not None else ""
    init_base_price = request.GET.get("init_base_price") if request.GET.get("init_base_price") is not None else ""
    end_base_price = request.GET.get("end_base_price") if request.GET.get("end_base_price") is not None else ""
    init_area = request.GET.get("init_area") if request.GET.get("init_area") is not None else ""
    end_area = request.GET.get("end_area") if request.GET.get("end_area") is not None else ""

    property = house_filter(query, property, garage, pool, backyard, init_base_price, end_base_price, init_area, end_area)

    context = {
        'title': 'Houses',
        'houses': property,
    }
    return context


def all_buildings_use_case(request):
    '''Buildings listing use case.'''
    query = request.GET.get("q") if request.GET.get("q") is not None else ""
    init_base_price = request.GET.get("init_base_price") if request.GET.get("init_base_price") is not None else ""
    end_base_price = request.GET.get("end_base_price") if request.GET.get("end_base_price") is not None else ""
    elevator = request.GET.get("elevator") if request.GET.get("elevator") is not None else ""
    concierge = request.GET.get("concierge") if request.GET.get("concierge") is not None else ""
    recreation_area = request.GET.get("recreation_area") if request.GET.get("recreation_area") is not None else ""
    buildings = get_all_buildings_infos(query, init_base_price, end_base_price, elevator, concierge, recreation_area)

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
