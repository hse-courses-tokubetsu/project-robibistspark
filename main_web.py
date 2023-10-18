#%% Query for user

from gensim.models import KeyedVectors
from navec import Navec
from transformers import AutoTokenizer, AutoModel

import pickle

from search import search
from load_indeces import (bm25, w2v_index, navec_index, bert_index)

w2v_model = KeyedVectors.load_word2vec_format('model.bin', binary=True)

navec = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')

tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/sbert_large_nlu_ru")
BERT_model = AutoModel.from_pretrained("sberbank-ai/sbert_large_nlu_ru")

#%% Load corpus
 
with open("corpus.pickle", "rb") as f:
    df = pickle.load(f)

#%% function

def make_query(query, index_type, n=2):
    
    if index_type == 'bm25':
        
        return search(query=query, index_type=index_type, model=bm25, 
                            corpus=df, n=n)
    
    elif index_type == 'w2v':
        
        return search(query=query, index_type=index_type, model=w2v_model, 
                      corpus=df, index=w2v_index, n=n)
    
    elif index_type == 'navec':
        
        return search(query=query, index_type=index_type, model=navec, 
                      corpus=df, index=navec_index, n=n)
    
    elif index_type == 'bert':
        
        return search(query=query, index_type=index_type, model=(tokenizer, 
                                                                 BERT_model), 
                      corpus=df, index=bert_index, n=n)    
    else:
        
        print('Invalid index type')