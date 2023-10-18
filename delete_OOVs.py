#%% Cleanse

def delete_OOVs(lemmas_list, model):
    clean = []
    for lemma in lemmas_list:
        try:
            model[lemma]
            clean.append(lemma)
        except KeyError:
            pass
    return clean