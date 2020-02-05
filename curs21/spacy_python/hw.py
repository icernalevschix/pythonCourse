import requests
from bs4 import BeautifulSoup
from collections import Counter
import spacy

url = 'https://www.python.org/dev/peps/pep-0020/'
page = BeautifulSoup(requests.get(url).content, 'html.parser')

nlp = spacy.load('en_core_web_sm')
Zen = nlp(page.find('div', id='the-zen-of-python').text)

#1. Find top ten most frequent words in text.

words = [token.text for token in Zen
         if not(token.is_stop or token.is_punct or token.is_space)]

print(Counter(words).most_common(10), end='\n\n#2.\n')

#2. Get list of unique words.

print(list(Counter(words)), end='\n\n#3.\n')

#3. Count number of nouns, adjectives and verbs.

nouns, adjectives, verbs = 0, 0, 0
for token in Zen:
    if token.pos_ == 'NOUN':
        nouns += 1
    elif token.pos_ == 'ADJ':
        adjectives += 1
    elif token.pos_ == 'VERB':
        verbs +=1

print(f'Nouns = {nouns}, Adjectives = {adjectives}, Verbs = {verbs} \n\n#4.')

#4. Find top 5 most used named entities in Zen of Python.

for ent in Zen.ents:
    print(ent.text, ent.label_)