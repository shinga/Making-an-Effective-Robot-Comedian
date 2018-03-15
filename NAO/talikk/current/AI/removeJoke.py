import pickle
from addJokes import *
filestring = "smallerObjects.p"

previousPickle = pickle.load(open(filestring,"rb"))

'''
for p in previousPickle:
    if p[0]._getName() == "":
        print "Found the perpetrator"
        previousPickle.remove(p)
'''

for p in previousPickle:
    print p 
    print "-----\n"



#pickle.dump(previousPickle,open(filestring,"wb"))

