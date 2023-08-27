from django import template
from beer.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    if Beer:
        return Category.objects.all()
    else:
        print('123')



