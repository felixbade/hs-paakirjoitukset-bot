import os

from dotenv import dotenv_values

from telegram import getMe, sendMessage
from scraper import get_latest_article

config = {
    **dotenv_values('.env'),
    **os.environ,
}

mandatory_variables = [
    'TELEGRAM_TOKEN',
    'TELEGRAM_CHAT'
]

for mandatory_variable in mandatory_variables:
    if not mandatory_variable in config:
        print(f'{mandatory_variable} needs to be set as an environment variable or in .env')
        exit(1)

link = get_latest_article()

tg_token = config['TELEGRAM_TOKEN']
tg_chat = config['TELEGRAM_CHAT']
print()
print(getMe(tg_token))
print()
print(sendMessage(tg_token, tg_chat, link))