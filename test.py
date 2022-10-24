
import numpy as np 
import pandas as pd 
import pickle
import re 
from collections import Counter
from nltk.tokenize import word_tokenize
path="df_data/phrases_data.df"
df=pickle.load(open(path,"rb"))
new_kw=[]
for ph in df["key_words"]:
    ph=ph.lower()
    ph=re.sub(r"[^a-z\s]",'',ph)
    new_kw.append(ph)
for i in df["key_words"]:
    print(i)



def get_frq(label:int,target:str):
    data=df[df["label"]==str(label)][target]
    res=[]
    for s in data:
        s=s.lower()
        s=re.sub(r"[^a-z\s]",'',s) #get ride of characters that are not letters.  
        tokens=word_tokenize(s)
        res.extend(tokens)
    return Counter(res)


