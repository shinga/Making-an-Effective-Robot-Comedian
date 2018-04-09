from graphviz import Digraph
import cPickle as pickle
import time
import random
from addJokes import *
'''

This is a depreciated and inactive file.

This was a performing script, that had a weird
idea for audience input. 

Binary input works better than this
'''
class heuristic(object):
    def __init__(self,name=None):
        if name is not None:
            self.name = name
        self.probability = 100
        self.failures = 0

    def giveFailGrade(self):
        self.failures+=1
        self.probability = self.probability / (2^self.failures)

    def getName(self):
        return self.name

class performance(object):
    def __init__(self):
    
        self.qualities =[ heuristic("romance"),
                        heuristic("Jobs"),
                        heuristic("Aging"),
                        heuristic("Human"),
                        heuristic("Robot"),
                        heuristic("length1"),
                        heuristic("length2"),
                        heuristic("length3") ]
        

    def updateHeuristics(hList=None,failure=False):
        if failure is True:
            for h in hList:
                for qual in qualities:
                    if h is qual.getName():
                        qual.giveFailGrade()
                        break

if __name__=="__main__":
    g = Digraph('Unconnected Jokes', filename="unconnectedJokes.gv")
    g.attr('node',shape='circle')
    random.seed()


    #this is the sim for getting audience input for jokes
    done = False
    setRespAvg = 0
    jokesTold = 0
    while not done: #loop for performance
        counter=0
        jokeRespAvg = 0
        for x in xrange(0,random.randrange(6,12)): #Samples in a joke told
            sample = random.randrange(0,32768) #simulated response from the microphones
            counter = counter + 1
            jokeRespAvg=(jokeRespAvg+sample)/counter


        #Averages of the performance
        jokesTold = jokesTold + 1
        print "Here is the Avg Resp from a joke:", jokeRespAvg
        print "Here is the Set Avg Resp:", setRespAvg
        setRespAvg=(setRespAvg+jokeRespAvg)/jokesTold
        
        if jokesTold > 5:
            done = True
        
    #prints the graph of all of the jokes
    temp = pickle.load(open("smallerObjects.p","rb"))
    for joke in temp:
        g.node(joke[0])
        print "\nHere is a joke obj:"
        print joke

    g.view()
