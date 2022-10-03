import requests
from bs4 import BeautifulSoup

userMovieName = input("Enter the movie you want: ")
res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.find_all('tr')
for tr in trs:
    movie = tr.find('td', {'class': 'titleColumn'})
    movie_name = movie.a.text.strip()
    if movie_name == userMovieName:
        movie_id = movie.a['href']
        movie_url = f'https://www.imdb.com/{movie_id}'
        print(movie_url)

        res2 = requests.get(movie_url)
        html = res2.text
        soup2 = BeautifulSoup(html, 'html.parser')
        li = soup2.find('li', {'data-testid': 'title-pc-principal-credit'})
        director_name = li.div.ul.li.a.text.strip()
        director_id = li.div.ul.li.a['href']
        director_url = f'https://www.imdb.com{director_id}'

        print(director_name, director_url)

        res3 = requests.get(director_url)
        html = res3.text
        soup3 = BeautifulSoup(html, 'html.parser')
        div = soup3.find('div', {'id':'knownfor'})
        movie_divs = div.find_all('div', {'class': 'knownfor-title'})
        recommended_movies = []
        for div in movie_divs:
            movie_name_div = div.find('div', {'class': 'knownfor-title-role'})
            recommended_movies.append(movie_name_div.a.text.strip())
        recommended_movies = ','.join(recommended_movies)

        print(recommended_movies)





        break



