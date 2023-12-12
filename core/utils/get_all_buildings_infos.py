from properties.models import Apartment, Building


def get_all_buildings_infos(query, init_base_price, end_base_price, elevator, concierge, recreation_area) -> list[Building]:
    '''Buildings infos listing '''
    if query is not None:
        buildings = Building.objects.filter(name__icontains=query) | Building.objects.filter(city__icontains=query)
    else:
        buildings = Building.objects.all()
    if elevator == "on":
        buildings = buildings.filter(elevator=True)
    if concierge == "on":
        buildings = buildings.filter(concierge=True)
    if recreation_area == "on":
        buildings = buildings.filter(recreation_area=True)

    for building in buildings:
        building.vacant = Apartment.objects.filter(vacant=True, building=building).count()
        building.min_price = Apartment.objects.filter(building=building).order_by('base_price').first()
        building.max_price = Apartment.objects.filter(building=building).order_by('-base_price').first()

    if init_base_price != "" and end_base_price != "":
        test = []
        for building in buildings:
            if building.min_price.base_price >= int(init_base_price) and building.max_price.base_price <= int(end_base_price):
                test.append(building)

        buildings = test

    return buildings


def get_home_buildings_info() -> list[Building]:
    '''Buildings infos listing for home page'''
    buildings = Building.objects.all()

    for building in buildings:
        building.vacant = Apartment.objects.filter(vacant=True, building=building).count()
        building.min_price = Apartment.objects.filter(building=building).order_by('base_price').first()

    return buildings
