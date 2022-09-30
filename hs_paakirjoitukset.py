import os
import time

from dotenv import dotenv_values

from telegram import get_me, send_message
from scraper import get_latest_articles
from article_db import ArticleDB

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

tg_token = config['TELEGRAM_TOKEN']
tg_chat = config['TELEGRAM_CHAT']

article_db = ArticleDB()

while True:
    links = get_latest_articles()
    links.reverse() # oldest first

    for link in links:
        if link not in article_db:
            article_db.add(link)
            resp = send_message(tg_token, tg_chat, link)
            if not resp.get('ok'):
                print(resp)
            print(f'New article: {link}')

    # The exact part of the minute will drift, but it doesn't matter
    time.sleep(60)