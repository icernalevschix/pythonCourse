import spacy
from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

nlp = spacy.load('en_core_web_sm')

MESH_DESCRIPTOR = 'https://id.nlm.nih.gov/mesh/lookup/descriptor'
MESH_API_DETAILS = 'https://id.nlm.nih.gov/mesh/lookup/details'

urls = [
'https://patient.info/forums/discuss/asthma-or-anxiety-need-a-bit-of-advice-please-724249',
'https://patient.info/forums/discuss/asthma-after-anaphylactic-reaction-719379',
'https://patient.info/forums/discuss/blood-pressure-meds-for-ears--723608',
'https://patient.info/forums/discuss/liver-inflammation-from-methotrexate-704988',
'https://patient.info/forums/discuss/after-ankle-surgery-724182',
'https://patient.info/forums/discuss/ankle-injury-724323',
'https://patient.info/forums/discuss/ankylosing-spondylitis-finger-stiffness-and-pain-707576',
'https://patient.info/forums/discuss/should-iincrease-dose-been-on-10mg-for-4-weeks-no-improvement--726975'
]

data = []

for url in urls:
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    title = soup.find('h1', class_="post__title").getText()
    content = soup.find(id='post_content').findChildren('p', recursive =False)[0].getText()

    data.append({'title':title, 'content':content})

def extract_nouns(text):
    words = set()
    for token in nlp(text):
        if not(token.is_punct or token.is_stop) and token.pos_ == 'NOUN':
            words.add(token.lemma_.strip().lower())
    return words


def find_medical_terms(term):
    r = requests.get(MESH_DESCRIPTOR, params={'label': term})
    if not(r.ok and r.json()):
        return ''
    return r.json()[0]['resource']


def extract_synonyms(url):
    path = urlparse(url).path
    descriptor = path.split('/')[-1]

    r = requests.get(MESH_API_DETAILS, params={'descriptor': descriptor})
    if not r.ok:
        return ''
    synonyms = ', '.join([x['label'] for x in r.json()['terms']])
    
    return synonyms

medical_terms = set()

for post in data:
    words = extract_nouns(post['content'])
    
    for word in words:
        descriptor = find_medical_terms(word)

        if(descriptor):
            print(extract_synonyms(descriptor))
