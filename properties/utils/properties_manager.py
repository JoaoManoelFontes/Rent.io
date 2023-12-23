from django.shortcuts import get_object_or_404
from properties.models import Building, House, Apartment
from properties.utils.create_graphic import create_graphics
from properties.utils.get_time_between_two_dates import get_time_between_two_dates
from properties.utils.validate_payment_date import validate_payment_date
from django.utils import timezone


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


def get_house_infos(house_id) -> House:
    '''Returns a house with its image and contract if it is not vacant'''
    house = get_object_or_404(House, pk=house_id)
    house.image = house.media.first().image
    house.expenses_amount = house.expenses.all().count()
    house.concluded_expenses = house.expenses.all().filter(done=True).count()
    house.pending_expenses = house.expenses.all().filter(done=False).count()
    house.expenses_total_value = sum(house.expenses.values_list("value", flat=True)) if house.expenses.all().count() > 0 else 0
    house.expenses_concluded_value = sum(house.expenses.all().filter(done=True).values_list("value", flat=True)) if house.expenses.all().count() > 0 else 0
    house.expenses_pending_value = sum(house.expenses.all().filter(done=False).values_list("value", flat=True)) if house.expenses.all().count() > 0 else 0
    if house.expenses.all().count() > 0:
        house.expenses_list = house.expenses.all()
    if not house.vacant:
        house.contracts = house.contract.get()
        if house.contracts.due_date < timezone.now().date():
            house.contract_expired = True
        else:
            house.contract_expired = False
        house.payment_day = house.contracts.base_payment_date.day
        house.payments_amount = house.payment.all().count()
        house.months_of_contract = get_time_between_two_dates(house.contracts.base_payment_date, house.contracts.due_date)
        house.contract_name = house.contracts.contract_file.name.split('/')[-1]
        house.payments = house.payment.all()
        house.total_value = sum(house.payments.values_list("value", flat=True)) if house.payments.all().count() > 0 else 0
        house.profit = house.total_value - house.expenses_concluded_value
        house.graphic = get_values_for_graphic(house)
    return house


def get_building_infos(building_id) -> Building:
    '''Returns a building with all infos'''
    building = get_object_or_404(Building, pk=building_id)
    building.image = building.media.first().image
    building.expenses_amount = building.expenses.all().count()
    building.concluded_expenses = building.expenses.all().filter(done=True).count()
    building.pending_expenses = building.expenses.all().filter(done=False).count()
    building.expenses_total_value = sum(building.expenses.values_list("value", flat=True)) if building.expenses.all().count() > 0 else 0
    building.expenses_concluded_value = sum(building.expenses.all().filter(done=True).values_list("value", flat=True)) if building.expenses.all().count() > 0 else 0
    building.expenses_pending_value = sum(building.expenses.all().filter(done=False).values_list("value", flat=True)) if building.expenses.all().count() > 0 else 0
    building.apartments = Apartment.objects.filter(building=building).count()
    building.apartments_occupied = Apartment.objects.filter(building=building, vacant=False).count()
    building.apartments_vacant = Apartment.objects.filter(building=building, vacant=True).count()
    building.apartments_late_payments = Apartment.objects.filter(building=building, late_payment=True).count()
    building.expenses_amount = building.expenses.all().count()
    if building.expenses.all().count() > 0:
        building.expenses_list = building.expenses.all()
    building.apartments_list = []
    if Apartment.objects.filter(building=building).count() > 0:
        building.total_value = 0
        for apartment in Apartment.objects.filter(building=building):
            ap_info = get_apartment_infos(apartment.id)
            building.apartments_list.append(get_apartment_infos(apartment.id))
            if not ap_info.vacant:
                building.total_value += ap_info.payments_total_value
        building.profit = building.total_value - building.expenses_concluded_value
    building.graphic = get_values_for_graphic(building)
    return building


def get_apartment_infos(apartment_id) -> Apartment:
    '''Returns an apartment with its contract and payments infos if it is not vacant'''
    apartment = get_object_or_404(Apartment, pk=apartment_id)
    if not apartment.vacant:
        apartment.contracts = apartment.contract.get()
        if apartment.contracts.due_date < timezone.now().date():
            apartment.contract_expired = True
        else:
            apartment.contract_expired = False
        apartment.payment_day = apartment.contracts.base_payment_date.day
        apartment.payments_amount = apartment.payment.all().count()
        apartment.last_payment = apartment.payment.all().last().base_payment_month if apartment.payment.all().count() > 0 else None
        apartment.months_of_contract = get_time_between_two_dates(apartment.contracts.base_payment_date, apartment.contracts.due_date)
        apartment.contract_name = apartment.contracts.contract_file.name.split('/')[-1]
        apartment.payments = apartment.payment.all()
        apartment.payments_total_value = sum(apartment.payments.values_list("value", flat=True)) if apartment.payments.all().count() > 0 else 0
        apartment.last_payment_date = apartment.payments.last().date if apartment.payments.all().count() > 0 else None
    else:
        apartment.payments = []
    return apartment


def get_apartment_list(building_id) -> list:
    '''Returns a list of apartments of a building'''
    apartments = map((lambda apartment: get_apartment_infos(apartment.id)), Apartment.objects.filter(building=building_id))
    return list(apartments)


def get_properties_list(customer) -> list:
    '''Returns a list of properties of a customer'''
    houses = map((lambda house: get_house_infos(house.id)), House.objects.filter(customer=customer))

    buildings = map((lambda building: get_building_infos(building.id)), Building.objects.filter(customer=customer))
    return list(houses) + list(buildings)


def get_values_for_graphic(property):
    '''Returns a list of values for the graphic'''
    if isinstance(property, House):
        payments = []
        months = []
        if not property.vacant:
            for i in range(1, 13):
                months.append(i)
                payments.append(sum(property.payments.filter(base_payment_month=i).values_list("value", flat=True)) if property.payments.filter(base_payment_month=i).values_list("value", flat=True) is not None else 0)
    else:
        payments = []
        months = []
        for i in range(1, 13):
            months.append(i)
            soma = 0
            for apartment in property.apartments_list:
                if not apartment.vacant:
                    soma += sum(apartment.payments.filter(base_payment_month=i).values_list("value", flat=True)) if apartment.payments.filter(base_payment_month=i).values_list("value", flat=True) is not None else 0
                    # print(soma)
            payments.append(soma)
    image = create_graphics(payments, months)
    return image
