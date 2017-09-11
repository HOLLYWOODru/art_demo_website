from django import template

register = template.Library()

@register.filter
def get_range(value, arg):

    if arg < value:
        return range(0, arg)

    return range(0, value)

@register.filter
def get_image_url(value, arg):

    return arg[value].image_url
