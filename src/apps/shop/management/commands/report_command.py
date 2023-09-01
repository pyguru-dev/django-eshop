from typing import Any, Optional
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'generate report '
    
    def handle(self, *args, **options):
        print('Generating excel report ...')