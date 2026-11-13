import time

from handlers import get_updates, send_message
from utils import str_to_float
from rates import convert


users = {}


def main() -> None:
    last_update_id = None

    while True:
        updates = get_updates(offset=last_update_id)

        for update in updates:

            message = update.get('message')
            if message:
                chat_id = message['chat']['id']

                text = message.get('text')
                if text:

                    if text.startswith('/start'):
                        first_name = message['from']['first_name']
                        welcome_message = f'salom {first_name}! botga xush kelibsiz.'
                        reply_markup = {
                            'keyboard': [
                                [{'text': 'USD->UZS'}, {'text': 'UZS->USD'}],
                                [{'text': 'RUB->UZS'}, {'text': 'UZS->RUB'}],
                                [{'text': 'EUR->UZS'}, {'text': 'UZS->EUR'}],
                            ]
                        }

                        send_message(chat_id, welcome_message, reply_markup)

                    elif text == 'USD->UZS':
                        users[chat_id] = 'USD->UZS'
                        print(users)

                    elif text == 'UZS->USD':
                        users[chat_id] = 'UZS->USD'
                        print(users)

                    elif text == 'RUB->UZS':
                        users[chat_id] = 'RUB->UZS'
                        print(users)

                    elif text == 'UZS->RUB':
                        users[chat_id] = 'UZS->RUB'
                        print(users)

                    elif text == 'EUR->UZS':
                        users[chat_id] = 'EUR->UZS'
                        print(users)

                    elif text == 'UZS->EUR':
                        users[chat_id] = 'UZS->EUR'
                        print(users)

                    else:
                        value = str_to_float(text)
                        if value is None:
                            send_message(chat_id, 'Iltimos son qiymat yuboring.')
                        else:
                            settings = users.get(chat_id)
                            if settings:
                                from_currency, to_currency = settings.split('->')
                                result = convert(
                                    value,
                                    from_currency,
                                    to_currency
                                )
                                send_message(chat_id, f'Natija: {result:,.2f} in {to_currency}')

                            else:
                                send_message(chat_id, 'qaysi valyutadan qaysiga.')

            last_update_id = update['update_id'] + 1

        time.sleep(0.3)


if __name__ == '__main__':
    main()
