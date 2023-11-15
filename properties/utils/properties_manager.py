from django.shortcuts import get_object_or_404
from properties.models import Building, House, Apartment
from properties.utils.get_time_between_two_dates import get_time_between_two_dates
from properties.utils.validate_payment_date import validate_payment_date


def get_properties_amount(customer) -> int:
    '''Returns the amount of properties of a customer'''

    return House.objects.filter(customer=customer).count() + Apartment.objects.filter(building__customer=customer).count()


def get_occupied_properties_amount(customer) -> int:
    '''Returns the amount of occupied properties of a customer'''

    return House.objects.filter(customer=customer, vacant=False).count() + Apartment.objects.filter(building__customer=customer, vacant=False).count()


def get_late_payments_amount(customer) -> int:
    '''Returns the amount of late payments of a customer'''
    houses = House.objects.filter(customer=customer)
    for house in houses:
        if not house.vacant:
            base_payment_month = house.payment.all().last().base_payment_month if house.payment.all().count() > 0 else -1
            base_payment_date = house.contract.get().base_payment_date

            if validate_payment_date(
                base_payment_month, base_payment_date
            ) is False:
                house.late_payment = True
                house.save()
            else:
                house.late_payment = False
                house.save()

    for apartment in Apartment.objects.filter(building__customer=customer):
        if not apartment.vacant:
            base_payment_month = apartment.payment.all().last().base_payment_month if apartment.payment.all().count() > 0 else -1
            base_payment_date = apartment.contract.get().base_payment_date
            if validate_payment_date(base_payment_month, base_payment_date) is False:
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
        house.image = house.media.first().image
        if not house.vacant:
            house.contracts = house.contract.get()

    buildings = Building.objects.filter(customer=customer)
    for building in buildings:
        building.image = building.media.first().image
        building.apartments = Apartment.objects.filter(building=building).count()
        building.apartments_occupied = Apartment.objects.filter(building=building, vacant=False).count()
        building.apartments_late_payments = Apartment.objects.filter(building=building, late_payment=True).count()
    return list(houses) + list(buildings)


def get_house_infos(house_id) -> House:
    '''Returns a house with its image and contract if it is not vacant'''
    house = get_object_or_404(House, pk=house_id)
    house.image = house.media.first().image
    if not house.vacant:
        house.contracts = house.contract.get()
        house.payment_day = house.contracts.base_payment_date.day
        house.payments_amount = house.payment.all().count()
        house.payment_day = house.contracts.base_payment_date.day
        house.months_of_contract = get_time_between_two_dates(house.contracts.base_payment_date, house.contracts.due_date)
        house.contract_name = house.contracts.contract_file.name.split('/')[-1]
    return house
