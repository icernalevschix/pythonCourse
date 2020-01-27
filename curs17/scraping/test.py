import requests

response = requests.get('http://api.dataatwork.org/v1/jobs')

# print(response.json())

for record in response.json():
    print(record['title'])