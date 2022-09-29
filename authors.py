from bs4 import BeautifulSoup
import requests

r = requests.get("https://quotes.toscrape.com/")
html = r.text
soup = BeautifulSoup(html, 'html.parser')

with open('author.csv', 'w') as f:
    for tag in soup.find_all('small', {'class': 'author'}):
        f.write(tag.text)
        f.write('\n')