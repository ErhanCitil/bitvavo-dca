from django.core.management.base import BaseCommand, CommandError
import os 
from dotenv import load_dotenv
from python_bitvavo_api.bitvavo import Bitvavo

class Command(BaseCommand):
    def handle(self, *args, **options):

        help = "Bitvavo DCA bot, die elke dag automatisch voor jou Bitcoins koopt volgens de DCA strategie."

        load_dotenv()
        BITVAVO_API_KEY = os.getenv("BITVAVO_API_KEY")
        BITVAVO_API_SECRET = os.getenv("BITVAVO_API_SECRET")

        bitvavo = Bitvavo({
            'APIKEY': BITVAVO_API_KEY,
            'APISECRET': BITVAVO_API_SECRET,
})
        
        balance = bitvavo.balance({'symbol': 'EUR'})

        if int(balance[0]['available']) >= 25:
            print("Je hebt genoeg geld om te investeren")
        else:
            print("Je hebt niet genoeg geld om te investeren")