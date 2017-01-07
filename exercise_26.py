import random
from urllib import urlopen     #urlopen, to open the url passed as param
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []                                                    # empty list

phrases = {                                                   # phrase dictionary
"class X(X):":
    "Make a class named X that is-a X.",
"class X(object):\n\tdef __init__(self, J):":
    "class X has-a the __init__ that takes self,J parameters",
"class X(object):\n\tdef $$$(self, J):":
    "class X has-a the $$$ that takes self, J as parameter",
"$$$ = X()":
    "Instantiate the $$$ to X",
"$$$ = X(J)":
    "Instantiate $$$ to X(J)",
"$$$.$$$ = '$$$'":
    "assign $$$ to $$$"
}

temp = urlopen(WORD_URL).readlines()
for i in temp:                                                # open the url, read the words and append to words list
    WORDS.append(i.strip())

def convert(snippet, phrase):                                 # converts the genral phrase values to random words from WORDS list
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count('X'))]
    other_names = random.sample(WORDS, snippet.count("M"))
    results = []
    temp = []
    param_pass = []

    for i in range(0, snippet.count("J")):
        param_count = random.randint(1,3)
        param_pass.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]
        for i in class_names:
            result = result.replace('X', i, 1)

        for k in other_names:
            result = result.replace("$$$", k, 1)

        for l in param_pass:
            result = result.replace('J', l, 1)

        results.append(result)

    return results

try:                                                       # it will call convert method if the param "hello" is passed
        snippets = phrases.keys()                          # along with the execution line
        random.shuffle(snippets)
        print sys.argv

        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if sys.argv[0] == 'hello':
                question, answer = answer, question

            print question
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"





