import requests

from config import CBU_TIMEOUT
from utils import str_to_float


def get_rate(currency: str = 'USD') -> float | None:
    url = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/{currency}/'

    response = requests.get(url, timeout=CBU_TIMEOUT)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            rate = str_to_float(data[0]['Rate'])
            if rate is None:
                raise ValueError('Rate qiymatini float ga convert qilib bolmadi.')
            return rate

        return None

    return None


def convert(value: float, from_currency: str, to_currency: str) -> float:

    if to_currency == 'UZS':
        rate = get_rate(from_currency)
        return round(value * rate, 2)

    rate = get_rate(to_currency)
    return round(value / rate, 2)
