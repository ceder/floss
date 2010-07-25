# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.simple_tag
def date_trans(dd):
    return 'dd'

            
