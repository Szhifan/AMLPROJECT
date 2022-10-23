1. align each phrase with its label through phrase id. 
2. normalize each label from [0,1] to classes ranging from 1 to 5. 
3. use stanza library to get the lemma of each word and select the verb, adjective,    adv  and word "not" of each phrase. Because we believe they carry the essential information about the label of the phrase. Also we removed stop words from the phrases using the stop word dictionary in NLTK. 


4. create a dataframe in path: df_data/phrases_data.df with the column: 
   ['id', 'phrase', 'lemma', 'key_words', 'label'], where key_words column contain the verbs, adj and adv of each phrase. 