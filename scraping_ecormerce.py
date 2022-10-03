import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

base_url = 'https://www.thewhiskyexchange.com'
product_links = []
for x in range(1, 4):
    res = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}')
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    product_list = soup.find_all('li', {'class':'product-grid__item'})
    

    for product in product_list:
        for link in product.find_all('a', href=True):
            product_links.append(base_url + link['href'])

for link in product_links:
    print(link)

for link in product_links:
    res = requests.get(link, headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h1', {'class':'product-main__name'}).text.strip()
    price = soup.find('p', {'class': 'product-action__price'}).text.strip()
    try:
        reviews = soup.find('span', {'class': 'review-overview__rating star-rating star-rating--40'}).span.text.strip()
    except:
        reviews = 'no rating'
    

    whisky = {
        'title': title,
        'reviews': reviews,
        'price': price,
    }
        
print(whisky)
    