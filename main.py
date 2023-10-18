#%% Query for user

from time import time
import pickle
import argparse

from search import search

#%% Load corpus
 
with open("corpus.pickle", "rb") as f:
    df = pickle.load(f)

#%% function

def make_query(query, index_type, n=2):
    
    if index_type == 'bm25':
        
        from load_indeces import bm25
        
        return search(query=query, index_type=index_type, model=bm25, 
                            corpus=df, n=n)
    
    elif index_type == 'w2v':
        
        from gensim.models import KeyedVectors
        w2v_model = KeyedVectors.load_word2vec_format('model.bin', binary=True)
        from load_indeces import w2v_index
        
        return search(query=query, index_type=index_type, model=w2v_model, 
                      corpus=df, index=w2v_index, n=n)
    
    elif index_type == 'navec':
        
        from navec import Navec
        navec = Navec.load('navec_news_v1_1B_250K_300d_100q.tar')
        from load_indeces import navec_index
        
        return search(query=query, index_type=index_type, model=navec, 
                      corpus=df, index=navec_index, n=n)
    
    elif index_type == 'bert':
        
        from transformers import AutoTokenizer, AutoModel
        
        tknr = AutoTokenizer.from_pretrained("sberbank-ai/sbert_large_nlu_ru")
        BERT = AutoModel.from_pretrained("sberbank-ai/sbert_large_nlu_ru")
        
        from load_indeces import bert_index
        
        return search(query=query, index_type=index_type, model=(tknr, BERT), 
                      corpus=df, index=bert_index, n=n)    
    else:
        
        print('Invalid index type')

#%% parser

parser = argparse.ArgumentParser(description="Make query")

parser.add_argument("query_text", type=str)
parser.add_argument("chosen_index", type=str)
parser.add_argument("docs_num", type=int)

args = parser.parse_args()

start = time()
    
result = make_query(query=args.query_text, index_type=args.chosen_index, 
                 n=args.docs_num)

end = time()

print(f'Execution time, s: {end - start}')
print()
print(result)