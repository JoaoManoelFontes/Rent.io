from django.shortcuts import render
from ..use_cases.home_use_cases import detail_house_use_case, home_use_case, detail_building_use_case


def home(request, pk=id):
    '''Properties listing view.'''
    return render(request, 'core/home.html', context=home_use_case())


def detail_building(request, pk=id):
    '''Building detail view.'''
    return render(request, 'core/detail_building.html', context=detail_building_use_case(pk))


def detail_house(request, pk=id):
    '''House detail view.'''
    return render(request, 'core/detail_house.html', context=detail_house_use_case(pk))
