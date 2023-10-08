from properties.models import Building, House, Apartment, Media
from properties.utils.validate_payment_date import validate_payment_date


def get_properties_amount(customer) -> int:
    '''Returns the amount of properties of a customer'''

    return House.objects.filter(customer=customer).count() + Building.objects.filter(customer=customer).count()


def get_occupied_properties_amount(customer) -> int:
    '''Returns the amount of occupied properties of a customer'''

    return House.objects.filter(customer=customer, vacant=False).count() + Apartment.objects.filter(building__customer=customer, vacant=False).count()


def get_late_payments_amount(customer) -> int:
    '''Returns the amount of late payments of a customer'''
    houses = House.objects.filter(customer=customer)
    for house in houses:
        if not house.vacant and house.payment.all().count() > 0:
            if validate_payment_date(
                house.payment.all().last().base_payment_month,
                house.contract.get().base_payment_date
            ) is False:
                house.late_payment = True
                house.save()
            else:
                house.late_payment = False
                house.save()

    for apartment in Apartment.objects.filter(building__customer=customer):
        if not apartment.vacant and apartment.payment.all().count() > 0:
            if validate_payment_date(
                apartment.payment.all().last().base_payment_month,
                apartment.contract.get().base_payment_date
            ) is False:
                apartment.late_payment = True
                apartment.save()
            else:
                apartment.late_payment = False
                apartment.save()

    return House.objects.filter(customer=customer, late_payment=True).count() + Apartment.objects.filter(building__customer=customer, late_payment=True).count()


def get_properties_list(customer) -> list:
    '''Returns a list of properties of a customer'''
    houses = House.objects.filter(customer=customer)
    for house in houses:
        setattr(house, 'image', house.media.get().image)
        if not house.vacant:
            setattr(house, 'contracts', house.contract.get())

    buildings = Building.objects.filter(customer=customer)
    for building in buildings:
        setattr(building, 'image', Media.objects.filter(building)[0].image)
        setattr(building, 'apartments', Apartment.objects.filter(building=building).count())
        setattr(building, 'apartments_occupied', Apartment.objects.filter(building=building, vacant=False).count())
        setattr(building, 'apartments_late_payments', Apartment.objects.filter(building=building, late_payment=True).count())
    return list(houses) + list(buildings)
