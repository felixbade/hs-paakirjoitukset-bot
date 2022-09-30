import requests
from bs4 import BeautifulSoup

url = 'https://www.hs.fi/paakirjoitukset/'

def get_latest_article():
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html5lib')

    articles = soup.find_all('article')
    for article in articles:
        if article.a:
            link = article.a['href']
            if not link.startswith('/paakirjoitukset/'):
                # Should not happen unless HS changes the page logic
                continue

            link = f'https://www.hs.fi{link}'

            # Only the first link is needed, the rest are discarded
            return link