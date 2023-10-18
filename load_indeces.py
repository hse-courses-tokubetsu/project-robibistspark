#%% Imports

import pickle

#%% Indeces

# BM-25Okapi index

with open("bm25.pickle", "rb") as f:
    bm25 = pickle.load(f)

# word2vec index

with open("w2v_index.pickle", "rb") as f:
    w2v_index = pickle.load(f)

# Navec index

with open("navec_index.pickle", "rb") as f:
    navec_index = pickle.load(f)

# BERT index


with open("bert_index.pickle", "rb") as f:
    bert_index = pickle.load(f)