import shelve
shelveFile = shelve.open('myshelvefile')
shelveFile['age'] = 22
shelveFile['name'] = 'Alice'
shelveFile.close()

shelveFile = shelve.open('myshelvefile')
print(shelveFile['age'])
print(shelveFile['name'])
shelveFile.close()