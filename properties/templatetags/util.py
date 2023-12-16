from django import template

from properties.models import Apartment, House

register = template.Library()


@register.filter
def get_house_instance(value) -> bool:
    '''Returns True if value is an instance of House, False otherwise.'''
    return isinstance(value, House)


@register.filter
def get_property_image(value) -> str:
    '''Returns the FIRST image of the House/Building instance.'''
    if value:
        return value.media.first().image.url


@register.filter
def get_property_second_image(value) -> str:
    '''Returns the SECOND image of the House/Building instance.'''
    if value:
        if value.media.all().count() > 1:
            return value.media.all()[1].image.url


@register.filter
def get_first_apartment_by_building(value):
    '''Returns the first apartment of the building.'''
    return Apartment.objects.filter(building=value).first().base_price


@register.filter
def split_contract_name(value):
    '''Returns the first word of the contract name.'''
    return value.split('/')[-1]
