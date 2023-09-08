from django.core.management.base import BaseCommand, CommandParser
from utils.faker import generate_posts

class GeneratePostFaker(BaseCommand):
    help = ''

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('count', type=int)
    
    def handle(self, *args, **options):
        generate_posts(options['count'])
        print("complete")