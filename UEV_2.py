# Выбрать любой сайт с каталогом товаров и написать парсер.
import requests
from bs4 import BeautifulSoup


URL = 'https://www.e-katalog.ru/k298.htm'
HEADERS = {
   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}


def get_html(url, params=''):
   return requests.get(url)

def get_content(html):
    comps = []
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='touchcarousel-container')
    for i, item in enumerate(items):
        refs = item.find_all('a')
        for a in refs:
            temp = a.get('title')
            if temp != None:
                comps.append(temp)
    while '' in comps:
        comps.remove('')
    print('Популярные модели ноутбуков на сайте https://www.e-katalog.ru:')
    print(*comps, sep = ", ")
    

html = get_html(URL).text
get_content(html)

# Популярные модели ноутбуков на сайте https://www.e-katalog.ru:
# Lenovo IdeaPad 5 14ALC05, Lenovo IdeaPad 5 14ALC05, HP Pavilion Gaming 16-a0000, HP Pavilion Gaming 16-a0000, Lenovo ThinkBook 15 G2 ARE, Lenovo ThinkBook 15 G2 ARE, Lenovo IdeaPad 5 Pro 16ACH6, Lenovo IdeaPad 5 Pro 16ACH6, Asus TUF Dash F15 FX516PM, Asus TUF Dash F15 FX516PM, HP Pavilion 15-eh1000, HP Pavilion 15-eh1000, Asus A571GT, Asus A571GT, HP 15s-eq2000, HP 15s-eq2000, Lenovo IdeaPad S145 15, Lenovo IdeaPad S145 15, Apple MacBook Pro 14 (2021), Apple MacBook Pro 14 (2021), Apple MacBook Pro 16 (2021), Apple MacBook Pro 16 (2021), HP 15s-eq1000, HP 15s-eq1000, Asus ExpertBook B1 B1500CEAE, 
# Asus ExpertBook B1 B1500CEAE, Apple MacBook Pro 13 (2020) M1, Apple MacBook Pro 13 (2020) M1



