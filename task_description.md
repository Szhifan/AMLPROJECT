## Data preprocessing

1. align each phrase with its label through phrase id. 
2. normalize each label from [0,1] to classes ranging from 1 to 5. 
3. use the Stanza library to get the lemma of each word and select the verb, adjective,    adv and word "not" of each phrase. Because we believe they carry the essential information about the label of the phrase. Also, we removed stop words from the phrases using the stop word dictionary in NLTK. 


4. create a dataframe in path: df_data/phrases_data.df with the column: 
   ['id', 'phrase', 'lemma', 'keywords', 'label'], where key_words column contain the verbs, adj and adv of each phrase. 

## Data exploration 

  We drew word cloud images for each class, and for both the lemma data and the key_word data, it turns out that the keywords are in fact more relevant with the label: 

### The word cloud for all the keywords in class 1: ### 

<img src="/Users/sunzhifan/Desktop/amlproject/figures/key_words-1.png" alt="key_words-1" style="zoom:50%;" />

### The word cloud for all the lemmas in class 1: 

<img src="/Users/sunzhifan/Desktop/amlproject/figures/lemma-1.png" alt="lemma-1" style="zoom:50%;" />



Note that in the word cloud for the keywords we can see a lot of adjectives that directly indicate the sentiments: bad, lack, predictable,

little, boring etc. Thus, we will use the words in the keywords to construct our features for predicting the labels. 


## Dealing with negation word. 
Our original data cannot capture the semantics of the negation words. For instance, given a comment: "it is not a good film." We expect it to be label as negative, but since "good" is in our model and that p(w=good|c=positive) is high, the probability that this phrase has negative sentiment is probably low. In order to catch the semantics of the negation, we devised a simple methods adopted from the one proposed in J.Daniel (2020) that if we encounter a negation word "not", we automatically add a "neg_" tag to all the following words in that phrase. Thus _"it is not a good film."_ will be _"It is not neg_a neg_good neg_film."_ . Then we will use words with negation suffix such as _neg_good_ as features. Note that we only use search for not as an indication of negation because words like: "don't", "doesn't" and so on are lemmatized as "do not" and "does not" by the Stanza lemmatizer. 
Thus, we apply the following process to all the keywords in the dataframe and create a new column called _neg_keywords_ where each keyword of the phrase are tagged with "neg_" suffix if they follow a negation word. 