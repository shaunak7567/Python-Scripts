import json
from difflib import get_close_matches

data=json.load(open("dat.json"))

def word_meaning(w):
    w=w.upper()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        print("Did you mean %s instead ?" %get_close_matches(w,data.keys())[0])
        new_word=input("Enter the word ")
        return word_meaning(new_word)
    else:
        return "The word does not exist in dictionary"

word=input("Enter the word You want the meaning for :")
meaning=word_meaning(word)
print(meaning)
