import requests

from config import TOKEN, TG_URL, TG_TIMEOUT


def get_updates(offset: int | None = None) -> list[dict]:
    url = TG_URL.format(token=TOKEN, method='getUpdates')

    payload = {
        'offset': offset
    }

    response = requests.post(
        url,
        json=payload,
        timeout=TG_TIMEOUT
    )
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()

        return data['result']

    return []


def send_message(chat_id: int | str, text: str, reply_markup: dict = {}) -> None:
    url = TG_URL.format(token=TOKEN, method='sendMessage')

    payload = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup
    }

    response = requests.post(
        url,
        json=payload,
        timeout=TG_TIMEOUT
    )
    response.raise_for_status()
