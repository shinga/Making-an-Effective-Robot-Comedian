import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict

d = cmudict.dict()

def countSyllables(word):

    count = 0
    print("Entry for " + word + ": " + str(d[word.lower()]) )

    diffPronounce = len(d[word.lower()])

    for char in d[word.lower()][0]:
        for element in char:
            if element[-1] in ['0','1','2']:
                count+=1
    return count


print "This Program counts the syllables in a word!"
print "Just type 'exit' when you are done."
print "\nAlso, 'exit' has two syllables"
while True:
	usrInput = raw_input("=>")
        print(countSyllables(usrInput))

        if usrInput == 'exit':
            print("goodbye!")
            break
