import os

current_directory = os.getcwd()
print(current_directory)

content = os.listdir(current_directory)
print(content)

entries = os.listdir('.')
print(entries)

entries = os.scandir('.')
print(entries)

for e in entries:
    print(e.name)

entries = os.listdir('../my_folder')
# entries = os.listdir(.\\my_folder)
print(entries)

pwd = os.getcwd()
entries = os.listdir(f'{pwd}')
# entries = os.listdir(f'{pwd}\\my_folder') Windows
print(entries)