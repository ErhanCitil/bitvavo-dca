from django.core.management.base import BaseCommand, CommandError
import os 
from dotenv import load_dotenv

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_dotenv()
        BITVAVO_API_KEY = os.getenv("BITVAVO_API_KEY")
        BITVAVO_API_SECRET = os.getenv("BITVAVO_API_SECRET")