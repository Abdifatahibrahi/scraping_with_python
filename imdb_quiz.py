import requests
from bs4 import BeautifulSoup










res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.find_all('tr')
for tr in trs:
        td1 = tr.find('td', {'class':'titleColumn'})
        name = td1.a
        movie_name = td1.a.string.strip()
        movie_year = td1.span.text.strip()

        td2 = tr.find('td', {'class': 'ratingColumn imdbRating'})
        rating = td2.strong.text
        movie_id = name.attrs['href']
        movie_url = f'https://www.imdb.com/{movie_id}'
        print(movie_url)
        
        res2 = requests.get(f'{movie_url}')
        html = res2.text

        soup2 = BeautifulSoup(html, 'html.parser')
        div1 = soup2.find('div', {'class':['sc-80d4314-2', 'iJtmbR']})
        dul = div1.find('ul')
        il = dul.find_all('li')
        movie_duration = il[2].text
        




        ul = soup2.find('div', {'class': 'ipc-chip-list__scroller'})
        li = ul.find_all('a', {'class':'ipc-chip--on-baseAlt'})
        generes = []
        for a in li:
            sp = a.span.text
            generes.append(sp)
        generes = ','.join(generes)
        print('Movie Name: ', movie_name)
        print('Duration', movie_duration)
        print('Generes', generes)
        print('Movie Year: ', movie_year)

        print("=======================")

        
       