import cPickle as pickle
from main_ai import *
temp = pickle.load(open("jokePickle.p","rb"))


for joke in temp:
    print "Here is a joke"
    joke._printInfo()
