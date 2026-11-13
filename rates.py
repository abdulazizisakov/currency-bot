import requests

from config import CBU_TIMEOUT


def get_rate(currency: str = 'USD') -> float | None:
    url = f'https://cbu.uz/uz/arkhiv-kursov-valyut/json/{currency}/'

    response = requests.get(url, timeout=CBU_TIMEOUT)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()
        if len(data) > 0:
            return float(data[0]['Rate'])
        return None

    return None
