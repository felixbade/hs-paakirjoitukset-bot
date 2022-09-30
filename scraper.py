import requests
from bs4 import BeautifulSoup

url = 'https://www.hs.fi/paakirjoitukset/'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html5lib')

articles = soup.find_all('article')
for article in articles:
    if article.a:
        link = article.a['href']
        if not link.startswith('/paakirjoitukset/'):
            # should not happen unless HS changes the page logic
            continue
        
        link = f'https://www.hs.fi{link}'
        print(link)