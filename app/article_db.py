import time

filename = 'articles.txt'

class ArticleDB:
    
    def __init__(self):
        self.loadDB()
    
    def loadDB(self):
        self.articles = []

        try:
            data = open(filename).read()
            for line in data.split('\n'):
                if not line:
                    continue
                date, link = line.split('] ')
                date = date[1:]
                self.articles.append([date, link])
        except FileNotFoundError:
            with open(filename, 'w'):
                pass
    
    def __contains__(self, link):
        for article in self.articles:
            if article[1] == link:
                return True
        return False
    
    def add(self, link):
        date = time.strftime('%Y-%m-%d %H:%M:%S %z')
        self.articles.append([date, link])
        with open(filename, 'a') as f:
            f.write(f'[{date}] {link}\n')