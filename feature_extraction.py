
import numpy as np 
import pandas as pd 
import pickle
import re 
from collections import Counter
from nltk.tokenize import word_tokenize
path="df_data/phrases_data.df"

df=pickle.load(open(path,"rb"))

def add_neg(ph:str):
    """
    This function adds "neg_" suffix to each word in the phrase when negation words: not 
    are detected.  
    """
    res=""
    if re.search(r"(\snot\s)|(^not\s)|(\snever\s)|(^never\s)",ph):
        tokens=word_tokenize(ph)
        n=len(tokens)
        pos=2**32-1 
        for i in range(n):
            
            if tokens[i]=="not":
                pos=i 
            if i>pos:
                res+="neg_{} ".format(tokens[i])
            else:
                res+=tokens[i]+" "

        return res 
    return ph 

features=[s[:-1] for s in open("features.txt","r").readlines()]
def bi_feature_vec(ph,features):
    """
    returns the feature vector of a phrase. The returned object is a np.array with binary
    values, each value correspond to the presence of the feature word in the phrase. 
    """
    tokens=word_tokenize(ph)
    n=len(features)
    vec=np.zeros(n)
    for i in range(n):
        if features[i] in tokens:
            vec[i]=1 
    return vec 
def count_feature_vec(ph,features):
    """
    returns the feature vector of a phrase. 
    """
    tokens=word_tokenize(ph)
    n=len(features)
    vec=np.zeros(n)
    counter=Counter(tokens)
    for i in range(n):
        if features[i] in counter.keys():
            vec[i]=counter[features[i]]
    return vec 
features=open("features.txt","w")
neg_features=open("neg_features.txt","r").readlines()
for f in neg_features:
    if not f.startswith("neg_"):
        features.write(f)
        

