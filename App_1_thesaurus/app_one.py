import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json","r"))
#loads a file object which is created by open

#print(data["rain"])

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        print( "Did you mean %s?"%get_close_matches(word, data.keys())[0])
        while True:
            ok=input("Is the new word the correct word? Reply with Y or N: ")
            if ok == "Y":
                
                return data[get_close_matches(word, data.keys())[0]]
                break
                
            elif ok == "N":
                
                return "Whoops sorry do not have that word "
                break
                

    else:
        return "Word is not in database."

word=input("Enter word:")
a=translate(word)
if type(a) ==str:
    print(translate(word))
else:
    for b in a:
        print(b)

#print(get_close_matches("rainn",data.keys())[0])

#using difflib


  