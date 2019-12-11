import csv
import os
from base64 import b64encode

data = [
['Age', 'Name', 'Hobby'],[18,'Bob', 'Hiking'], [11,'123', '1223']
]

with open('write_data.csv', 'w', newline='\n') as csvfile: # or newline='' - pt windows ( ambele variante )
    csv_writer = csv.writer(csvfile)
    for d in data:
        csv_writer.writerow(d)

rand_string = os.urandom(5)
print(b64encode(rand_string).decode('utf-8'))
