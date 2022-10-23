import re 
def add_not_flag(sentence:list):
    not_flag=False 
    n=len(sentence)
    for i in range(n):
        if sentence[i]=="not":
            not_flag=True 
        if not_flag:
            sentence[i]="NOT_"+sentence[i]
        if re.search(r"[\.\?!]",sentence[i]):
            not_flag=False 
    return sentence 