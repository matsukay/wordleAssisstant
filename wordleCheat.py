import re
import sys
import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words

def main():

    dictionary = words.words()
    pattern = re.sub('[^a-zA-Z]', '.', sys.argv[1])
    a = re.compile("^" + pattern + "$", re.IGNORECASE)
    nr = 0
    results = []
    for w in dictionary:
        if a.match(w) != None:
            nr += 1
            results.append(w)
    
    if len(sys.argv) == 3:
        empty = sum(1 for char in sys.argv[1] if not char.isalpha())
        if len(sys.argv[2]) <= empty:
            finalResults = []
            for i in sys.argv[2]: 
                for r in results:
                    if i in r:
                        finalResults.append(r)
                    else:
                        nr -= 1
            message = "match found" if nr == 1 else "matches found"
            print(nr, message)
            print(finalResults)
        else:
            print("Invalid clue, are you sure you have the right number of characters?")
    else :
        message = "match found" if nr == 1 else "matches found"
        print(nr, message)
        print(results)



if __name__== "__main__":

    if len(sys.argv) >= 2 and len(sys.argv) <= 3:
        main()
    else:
        print("usage ./wordleCheat <pattern> <letters>")
        sys.exit(0)
    


# Write clues as ab___
# Use underscore for letters which are not sure
# For letters that are included but not certain about position, write them consecutively, 'ab'
# Can have either 2 or 3 arguments
# py wordleCheat.py ch___
# OR
# py wordleCheat.py ch___ i

