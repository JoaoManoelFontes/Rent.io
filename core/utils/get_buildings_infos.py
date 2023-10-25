from properties.models import Apartment, Building


def get_buildings_infos() -> list[Building]:
    '''Buildings infos listing '''
    buildings = Building.objects.all()
    for building in buildings:
        building.vacant = Apartment.objects.filter(vacant=True, building=building).count()
        building.min_price = Apartment.objects.filter(building=building).order_by('base_price').first()

    return buildings
