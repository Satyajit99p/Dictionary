import json
from difflib import get_close_matches

data= json.load(open("C:/Users/SATYAJIT/Desktop/dictionary.json"))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        yn=input("did you mean % s instead ? Enter Y is yes or N if no:"% get_close_matches(w,data.keys())[0])
        yn=yn.lower()
        if yn == 'Y':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == 'N':
            return "The word doesnt exist .Please double check it."
        else:
            return " We didn't understand your entry "
    else:
        return "The word doesnt exist .Please double check it."

word=input("Enter word : ")
output=translate(word)
if type(output)==list:
    for item in output:
        print (item)
else:
    print(output)
input('press ENTER to exit')


