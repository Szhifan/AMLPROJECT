import math
import re
import pandas as pd 
import pickle 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tqdm
import stanza 
# align phrase with label through phrase id 
path_dictionary="original_data/dictionary.txt"
path_label="original_data/sentiment_labels.txt"
text_dic=open(path_dictionary,"r").readlines()
reg=r"(.*)\|(.*)"
phrases=sorted([re.search(reg,i).groups() for i in text_dic],key=lambda x:int(x[1]))
text_labels=open(path_label,"r").readlines()
labels=sorted([re.search(reg,i).groups() for i in text_labels],key=lambda x:int(x[0]))

# labels=[(i[0],str(math.ceil(float(i[1])*5))) for i in labels]
# phrase_to_label=[(phrases[i][1],phrases[i][0],labels[i][1]) for i in range(len(labels))]
# df=pd.DataFrame(phrase_to_label)
# df.columns=["id","phrase","label"]
# pickle.dump(df,open("df_data/phrase_to_label.df","wb"))

# path_ph_2_lab="df_data/phrase_to_label.df"
# df=pickle.load(open(path_ph_2_lab,"rb"))
# phrases=df["phrase"]

def replace_stop_words(phrase:str):
    """
    This function replaces all the stop words in English. 
    """
    stop_words=set(stopwords.words("english"))
    tokens=word_tokenize(phrase)
    res=""
    for w in tokens:
        w=w.lower()
        w=re.sub(r"[^a-z\s]",'',w)
        if w not in stop_words:
            res+=w+' '
    return res 
def get_lemma_and_tag(phrase:str):
    """
    This function convert each token to lemma and extract adverbs, verbs, negation and adjectives. 
    """
    nlp=stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma', use_gpu=True) 
    lemma_phrase=""
    tag_phrase=""
    if not re.search(r"[a-zA-Z]",phrase): #if the phrases consists only of punctuations, we don't precess it with stanza
        lemma_phrase=phrase
    else:
        nlp_doc=nlp(phrase)
        for s in nlp_doc.sentences:
            for w in s.words:
                lemma=w.lemma 
                try: 
                    lemma_phrase+=lemma+" "
                except TypeError:
                    lemma=w.text
                    lemma_phrase+=lemma+" " 
                if w.upos=="ADJ" or w.upos=="VERB" or w.text=="not" or w.upos=="ADV" or w.text=="never": 
                    tag_phrase+=lemma+" "
    return lemma_phrase,tag_phrase
    

