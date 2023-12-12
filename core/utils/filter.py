def house_filter(query, house, garage, pool, backyard, init_base_price, end_base_price, init_area, end_area):
    '''House filter use case.'''
    house = house.filter(city__icontains=query)
    if garage == "on":
        house = house.filter(garage=True)
    if pool == "on":
        house = house.filter(pool=True)
    if backyard == "on":
        house = house.filter(backyard=True)
    if init_base_price != "" and end_base_price != "":
        house = house.filter(base_price__gte=init_base_price, base_price__lte=end_base_price)
    if init_area != "" and end_area != "":
        house = house.filter(area__gte=init_area, area__lte=end_area)
    return house
