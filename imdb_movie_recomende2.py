import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.imdb.com/chart/top/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
user_movie_name = input("Enter the name of the movie you want: ")

tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.find_all('tr')
for tr in trs:
    title_column = tr.find('td', {'class': 'titleColumn'})
    movie_id = title_column.a['href']
    movie_name = title_column.a.text.strip()
    movie_url = f"https://www.imdb.com{movie_id}"
    if user_movie_name == movie_name:
        print(movie_name, movie_url)

        res2 = requests.get(movie_url)
        html = res2.text
        soup2 = BeautifulSoup(html, 'html.parser')  
        div = soup2.find('div', {'class': 'ipc-metadata-list-item__content-container'})
        director_id = div.ul.li.a['href']
        director_url = f'https://www.imdb.com{director_id}'
        director_name = div.ul.li.a.text.strip()
        print(director_name, director_url)

        res3 = requests.get(director_url)
        html = res3.text
        soup3 = BeautifulSoup(html, 'html.parser')
        div = soup3.find('div', {'id':'knownfor'})
        div2 = div.find_all('div', {'class': 'knownfor-title'})
        for div in div2:
            moviename_div = div.find('div', {'class': 'knownfor-title-role'})
            movie_name = moviename_div.a.text.strip()
            print(movie_name)
        break




