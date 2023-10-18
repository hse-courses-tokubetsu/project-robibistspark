#%% Preprocessing

from nltk.corpus import stopwords
from spacy import load

stops = stopwords.words('russian')
nlp = load("ru_core_news_lg")

def preprocess_text(text: str, pos_needed=False) -> str:
    doc = nlp(text)
    
    text_lemmas = []
    if pos_needed is False:
        for sent in doc.sents:
            for i in sent: 
                if i.text.isalpha() is True \
                    and i.text not in stopwords.words('russian') \
                        and i.pos_ in ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB']:
                    text_lemmas.append(i.lemma_)
    elif pos_needed is True:
        for sent in doc.sents:
            for i in sent: 
                if i.text.isalpha() is True \
                    and i.text not in stopwords.words('russian') \
                        and i.pos_ in ['ADJ', 'ADV', 'NOUN', 'PROPN', 'VERB']:
                    text_lemmas.append(i.lemma_ + '_' + i.pos_)
    
    return text_lemmas