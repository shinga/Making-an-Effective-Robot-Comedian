import cPickle as pickle
from jokeObj import joke
fd = open("funnyJokes.p","rb")
jokes = pickle.load(fd )
for j in jokes:
    print j.getQualities()
fd.close() 
