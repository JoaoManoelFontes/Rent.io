def house_filter(query, houses, garage, pool, backyard, base_price, area):
    '''House filter use case.'''
    houses = houses.filter(city__icontains=query)
    if garage == "on":
        houses = houses.filter(garage=True)
    if pool == "on":
        houses = houses.filter(pool=True)
    if backyard == "on":
        houses = houses.filter(backyard=True)
    if base_price != "":
        houses = houses.filter(base_price__lte=base_price)
    if area != "":
        houses = houses.filter(area__lte=area)
    return houses
