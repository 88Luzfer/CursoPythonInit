import json
from difflib import get_close_matches

data = json.load(open("archivos/data.json"))

def translate (w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Dis you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "Thanks for use the program, use it again"
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)