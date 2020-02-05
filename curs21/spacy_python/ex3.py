import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

# about_interest_text = ('He is at work')
# about_interest_doc = nlp(about_interest_text)
# displacy.serve(about_interest_doc, style='dep')


piano_text = 'Gus is learning piano'
piano_doc = nlp(piano_text)
for token in piano_doc:
    print (token.text, token.tag_, token.head.text, token.dep_)

conference_text = ('There is a developer conference'
' happening on 21 July 2019 in London.')
conference_doc = nlp(conference_text)
for chunk in conference_doc.noun_chunks:
    print(chunk)


piano_class_text = ('Great Piano Academy is situated'
' in Mayfair or the City of London and has'
' world-class piano instructors.')
piano_class_doc = nlp(piano_class_text)
for ent in piano_class_doc.ents:
    print(ent.text, ent.start_char, ent.end_char,
            ent.label_, spacy.explain(ent.label_))

displacy.serve(piano_class_doc, style='ent')