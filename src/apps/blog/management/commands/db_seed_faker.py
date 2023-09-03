from typing import Any, Optional
from django.core.management.base import BaseCommand
from utils.faker import generate_posts

class GeneratePostFaker(BaseCommand):
    help = ''
    
    def handle(self, *args, **options):
        generate_posts(100)
        print("complete")