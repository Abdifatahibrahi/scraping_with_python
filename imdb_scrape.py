import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/chart/top/')
html = res.text

soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class':'lister-list'})
trs = tbody.find_all('tr')

for tr in trs:
    td = tr.find('td', {'class':'titleColumn'})
    movie_name = td.a.string
    movie_year = td.span.string
    movie_id = td.a['href']
    movie_url = f'https://www.imdb.com/{movie_id}'
    print(movie_name, movie_year, movie_url)

    

