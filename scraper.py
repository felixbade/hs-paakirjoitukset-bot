import os

import requests
from bs4 import BeautifulSoup
from dotenv import dotenv_values

from telegram import getMe, sendMessage

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

url = 'https://www.hs.fi/paakirjoitukset/'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html5lib')

article_links = []
articles = soup.find_all('article')
for article in articles:
    if article.a:
        link = article.a['href']
        if not link.startswith('/paakirjoitukset/'):
            # should not happen unless HS changes the page logic
            continue
        
        link = f'https://www.hs.fi{link}'
        article_links.append(link)
        print(link)

tg_token = config['TELEGRAM_TOKEN']
tg_chat = config['TELEGRAM_CHAT']
print()
print(getMe(tg_token))
print()
print(sendMessage(tg_token, tg_chat, article_links[0]))