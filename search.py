#%% Search

import numpy as np
from numpy.linalg import norm

from nltk import sent_tokenize
from torch import no_grad

from preprocess_text import preprocess_text
from delete_OOVs import delete_OOVs

def encode(sent, tokenizer, model):
    for s in [sent]:
        encoded_input = tokenizer(s, padding=True, truncation=True, max_length=64, return_tensors='pt')
        with no_grad():
            model_output = model(**encoded_input)
    
    return model_output[0][0][0].numpy()

def search(query, index_type, model, corpus, index=None, n=2):
    
    if index_type == 'bm25':
        
        clean_query = preprocess_text(query)
        
        ranked_docs = model.get_top_n(clean_query, corpus.text, n=n)
    
        return ranked_docs
    
    elif index_type == 'w2v':
        
        clean_query = delete_OOVs(preprocess_text(query, pos_needed=True), 
                                  model=model)
        
        query_vector = np.mean(model[clean_query], axis=0)
        
        cos_sims = np.dot(index, query_vector) / \
            (norm(index, axis=1) * norm(query_vector))
        
        d = {}
        for i, j in enumerate(cos_sims):
            d[i] = j
        ranking = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
        return [corpus['text'][ranking[i][0]] for i in range(n)]
        
    elif index_type == 'navec':
        
        clean_query = delete_OOVs(preprocess_text(query), model=model)
        
        vec = np.zeros((1, 300))
        for word in clean_query:
            vec += model[word]
        query_vector = vec / len(clean_query)
        
        cos_sims = np.dot(index, query_vector.transpose()) / \
            (norm(index, axis=1) * norm(query_vector))
        
        d = {}
        for i, j in enumerate(cos_sims):
            d[i] = j[0]
        
        ranking = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return [corpus['text'][ranking[i][0]] for i in range(n)]
    
    elif index_type == 'bert':
        
        vec = np.zeros((1, 1024))
        query_list = sent_tokenize(query)
        for sent in query_list:
            vec += encode(sent, model[0], model[1])
        query_vector = vec / len(query_list)
        
        cos_sims = np.dot(index, query_vector.transpose()) / \
            (norm(index, axis=1) * norm(query_vector))
        
        d = {}
        for i, j in enumerate(cos_sims):
            d[i] = j[0]
        
        ranking = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return [corpus['text'][ranking[i][0]] for i in range(n)]