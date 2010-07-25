# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def date_filters(user):
    return user

            
