# 3. Download content of 999.md site, calculate how many urls are present on it.

from urllib.request import urlopen

response = urlopen('https://999.md/')

nr = 0
for line in response:
    nr += line.decode().count('href="https')

print(f'Total number of urls: {nr}')