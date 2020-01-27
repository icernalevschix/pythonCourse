import requests
from bs4 import BeautifulSoup
import json
import time

url = 'https://999.md/ru/list/phone-and-communication/mobile-phones?view_type=detail'
base_url = 'https://999.md'
data = []
counter = 0

while counter<20:
    time.sleep(1.1)
    counter+=1

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

# parse data from the current page
    results = soup.find_all('li', class_='ads-list-detail-item')
    for post in results:
        try:
            title = post.find('div', class_='ads-list-detail-item-title').find('a').text.strip()
            price = post.find('div', class_='ads-list-detail-item-price').text.strip()
            description = post.find('div', class_='ads-list-detail-item-intro').text.replace('\n','').strip()
            data.append({'title': title, 'price': price, 'description': description})
        except AttributeError:
            pass

# find next page 
    try:
        next_page = soup.find('nav', class_='paginator cf').find('li', class_='current').findNext('li').find('a')['href']
        url = base_url + next_page
    except TypeError:
        break

    
with open('999_data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)