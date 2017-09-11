from django import template
import random

register = template.Library()

@register.filter
def get_random_number(start, stop):

    return random.randrange(start, stop)