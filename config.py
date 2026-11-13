import os

from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
TG_TIMEOUT = int(os.getenv('TG_TIMEOUT'))

TG_URL = 'https://api.telegram.org/bot{token}/{method}'
