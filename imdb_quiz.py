import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/title/tt0068646/')
html = res.text

soup2 = BeautifulSoup(html, 'html.parser')
div1 = soup2.find('div', {'class':['sc-80d4314-2', 'iJtmbR']})
dul = div1.find('ul')
il = dul.find_all('li')
movie_year = il[0].span.text
movie_rating = il[1].span.text
movie_duration = il[2].text
print(movie_year, movie_rating, movie_duration)

# dli = dul.find_all('li')
# print(dli)
# for i in dli:
    
# movie_year = dli[0].text.strip()
# movie_rating = dli[1].text.strip()
# movie_duration = dli[2].text.strip()
# print(movie_year, movie_rating, movie_duration)


ul = soup2.find('div', {'class': 'ipc-chip-list__scroller'})
li = ul.find_all('a', {'class':'ipc-chip--on-baseAlt'})
generes = []
for a in li:
    sp = a.span.text
    generes.append(sp)
generes = ','.join(generes)
print(generes)








# res = requests.get('https://www.imdb.com/chart/top/')
# html = res.text
# soup = BeautifulSoup(html, 'html.parser')



# tbody = soup.find('tbody', {'class': 'lister-list'})
# trs = tbody.find_all('tr')
# for tr in trs:
#         td1 = tr.find('td', {'class':'titleColumn'})
#         name = td1.a
#         year = td1.span

#         td2 = tr.find('td', {'class': 'ratingColumn imdbRating'})
#         rating = td2.strong.text
#         movie_id = name.attrs['href']
#         movie_url = f'https://www.imdb.com/{movie_id}'
#         print(movie_url)
       