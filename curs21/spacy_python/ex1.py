import spacy
import en_core_web_sm

nlp = en_core_web_sm.load()

about_text = ('Gus Proto is a Python developer currently'
' working for a London-based Fintech'
' company. He is interested in learning'
' Natural Language Processing.')
about_doc = nlp(about_text)
# sentences = list(about_doc.sents)
# print(len(sentences))
# for sentence in sentences:
#     print(sentence)

def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc

ellipsis_text = ('Gus, can you, ... never mind, I forgot'
' what I was saying. So, do you think'
' we should ...')
custom_nlp = spacy.load('en_core_web_sm')
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)

for sentence in custom_ellipsis_sentences:
    print(sentence)

# for token in about_doc:
#     print(token, token.idx, token.shape_, token.is_punct, token.is_space, token.is_stop)

spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
print(len(spacy_stopwords))
# for stop_word in list(spacy_stopwords)[:3]:
#     print(stop_word)

conference_help_text = ('Gus is helping organize a developer'
'conference on Applications of Natural Language'
' Processing. He keeps organizing local Python meetups'
' and several internal talks at his workplace.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print(token, token.lemma_)