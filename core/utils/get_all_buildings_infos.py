from properties.models import Apartment, Building


def get_all_buildings_infos(query) -> list[Building]:
    '''Buildings infos listing '''
    if query is not None:
        buildings = Building.objects.filter(name__icontains=query)
    else:
        buildings = Building.objects.all()

    for building in buildings:
        building.vacant = Apartment.objects.filter(vacant=True, building=building).count()
        building.min_price = Apartment.objects.filter(building=building).order_by('base_price').first()

    return buildings
