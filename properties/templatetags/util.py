from django import template

from properties.models import House

register = template.Library()


@register.filter
def get_house_instance(value) -> bool:
    '''Returns True if value is an instance of House, False otherwise.'''
    return isinstance(value, House)


@register.filter
def get_property_image(value) -> str:
    '''Returns the FIRST image of the House/Building instance.'''
    return value.media.first().image.url


@register.filter
def get_property_second_image(value) -> str:
    '''Returns the SECOND image of the House/Building instance.'''
    return value.media.all()[1].image.url
