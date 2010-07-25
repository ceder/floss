# -*- coding: iso-8859-2 -*-
 
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "clears django cache"

    def handle_noargs(self, **options):
        from django.core.cache import cache
        cache.clear()
