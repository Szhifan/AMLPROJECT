## Data preprocessing

1. align each phrase with its label through phrase id. 
2. normalize each label from [0,1] to classes ranging from 1 to 5. 
3. use the Stanza library to get the lemma of each word and select the verb, adjective,    adv and word "not" of each phrase. Because we believe they carry the essential information about the label of the phrase. Also, we removed stop words from the phrases using the stop word dictionary in NLTK. 


4. create a dataframe in path: df_data/phrases_data.df with the column: 
   ['id', 'phrase', 'lemma', 'key_words', 'label'], where key_words column contain the verbs, adj and adv of each phrase. 

## Data exploration 

  We drew word cloud images for each class, and for both the lemma data and the key_word data, it turns out that the keywords are in fact more relevant with the label: 

### The word cloud for all the keywords in class 1: ### 

<img src="/Users/sunzhifan/Desktop/amlproject/figures/key_words-1.png" alt="key_words-1" style="zoom:50%;" />

### The word cloud for all the lemmas in class 1: 

<img src="/Users/sunzhifan/Desktop/amlproject/figures/lemma-1.png" alt="lemma-1" style="zoom:50%;" />



Note that in the word cloud for the keywords we can see a lot of adjectives that directly indicate the sentiments: bad, lack, predictable,

little, boring etc. Thus, we will use the words in the keywords to construct our features for predicting the labels. 
