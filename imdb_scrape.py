import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/chart/top/')
html = res.text

soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.find_all('tr')
for tr in trs:
    td = tr.find('td', {'class':'titleColumn'})
    movie_name = td.a.text
    year = td.span.text
    print(movie_name, year)
