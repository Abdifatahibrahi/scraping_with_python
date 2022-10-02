import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.imdb.com/chart/top/")
html = res.text
soup = BeautifulSoup(html, 'html.parser')
tbody = soup.find('tbody', {'class': 'lister-list'})
trs = tbody.find_all('tr')
for tr in trs:
    trdetail = tr.find('td', {'class': 'titleColumn'})
    movie_name = trdetail.a.text.strip()
    movie_year = trdetail.span.text.strip()
    movie_id = trdetail.a['href']
    movie_url = f'https://www.imdb.com{movie_id}'

    res2 = requests.get(movie_url)
    html = res2.text
    soup2 = BeautifulSoup(html, 'html.parser')
    ul = soup2.find('ul', {'data-testid': 'hero-title-block__metadata'})

    li = ul.find_all('li')
    movie_duration = li[2].text.strip()

    generes = soup2.find('div', {'class': 'ipc-chip-list__scroller'})
    list = generes.find_all('a')
    generes_list = []
    for l in list:
        generes_list.append(l.text.strip())

    generes_list = ','.join(generes_list)
    

    print('Movie Name: ', movie_name)
    print('Movie Year: ', movie_year)
    print('Movie Duration: ', movie_duration)
    print('Movie genere: ', generes_list)
    print("==============================")