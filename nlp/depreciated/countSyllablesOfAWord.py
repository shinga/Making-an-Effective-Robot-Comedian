'''
This program just counts syllables
It looks up a word in a dictionary, 
where the syllables were counted before
'''
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict

d = cmudict.dict()

def countSyllables(word):

    count = 0
    print("Entry for " + word + ": " + str(d[word.lower()]) )
    for char in d[word.lower()]:
        for element in char:
            if element[-1] in ['0','1','2']:
                count+=1
    return count

while True:
	usrInput = raw_input("=>")
        print(countSyllables(usrInput))

        if usrInput == 'exit':
            print("goodbye!")
            break
