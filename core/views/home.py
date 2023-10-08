from django.shortcuts import render
from properties.models import Apartment, House, Building


def home(request, pk=id):
    '''Properties listing view.'''
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
    return render(request, 'core/home.html', context=context)


def vacant(request, pk=id):
    vacant = Apartment.objects.filter(vacant=True, building=pk).count()
    context = {
        'title': 'Vacant',
        'vacant': vacant,
    }
    return render(request, 'core/home.html', context=context)


def buildings(request):
    buildings = Building.objects.all()
    return render(request, 'core/buildings.html', context={
        'title': 'Buildings',
        'buildings': buildings,
    })


def houses(request):
    houses = House.objects.all()
    return render(request, 'core/houses.html', context={
        'title': 'Houses',
        'houses': houses,
    })
