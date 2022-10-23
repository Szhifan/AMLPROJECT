from sre_parse import Tokenizer
import stanza
import pandas as pd
import pickle
import tqdm 
import re 
from nltk import tokenize 
from matplotlib import pyplot as pp 
from collections import Counter
# nlp = stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma', use_gpu=True)
path_ph_data="df_data/phrases_data.df"
df=pickle.load(open(path_ph_data,"rb"))

def get_lemma_frq(label:int):
    lemma_class=df[df["label"]==str(label)]["lemma"].tolist()
    res=[]
    for s in lemma_class:
        print(s)

get_lemma_frq(3)



 