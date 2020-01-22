# import urllib.request
import requests
from bs4 import BeautifulSoup
import csv, json

url = 'https://www.rabota.md/search/?query=python&searchType=1&cityID=1'

# with urllib.request.urlopen(url) as f:
#     print(f.read(300).decode('utf-8'))

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='preview')

data = []

for job in results:
    h3 = job.find('h3')
    company_data = job.find('div')
    if h3 and company_data:            
        title = job.find('h3').find('a', class_='vacancy').text
        company = company_data.text.split('•')[0].strip()
        location = company_data.text.split('•')[1].strip()
        description = job.find('p').text.replace('\n','').strip()
        salary = job.find_all('span')[-1].text.strip()
        # print(title, ' - ',company, ' - ', location, end='\n\n')

        data.append({'title': title, 'company': company, 'location': location,
            'description': description, 'salary': salary
        })

# print(data)

# with open('new_file.csv', 'w', newline='', encoding='utf-8') as f:
#     keys = data[0].keys()
#     dict_writer = csv.DictWriter(f, fieldnames = keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(data)

with open('jobs.json', 'w') as json_file:
    json.dump(data, json_file)