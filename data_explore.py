import stanza
import pandas as pd
import pickle
import tqdm 
import re 
from nltk.tokenize import word_tokenize
from matplotlib import pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
# nlp = stanza.Pipeline('en', processors='tokenize,mwt,pos,lemma', use_gpu=True)
path_ph_data="df_data/phrases_data.df"
df=pickle.load(open(path_ph_data,"rb"))




def get_frq(label:int,target:str):
    data=df[df["label"]==str(label)][target]
    res=[]
    for s in data:
        s=s.lower()
        s=re.sub(r"[^a-z\s]",'',s) #get ride of characters that are not letters.  
        tokens=word_tokenize(s)
        res.extend(tokens)
    return Counter(res)
def generate_word_cloud(label:int,target):
    save_path="figures/{}-{}".format(target,label)
    text=""
    data=df[df["label"]==str(label)][target]
    for s in data:
        s=s.lower()
        s=re.sub(r"[^a-z\s]",'',s)
        text+=s+" " 
    
    wc=WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(text)
    plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad = 0)
  
    plt.savefig(save_path)

