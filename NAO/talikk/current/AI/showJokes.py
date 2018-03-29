from graphviz import Digraph
import cPickle as pickle
from main_ai import *
from flask import Flask, jsonify
from flask_cors import CORS
from sets import Set
import time
import random
from main_ai import *
app = Flask(__name__)
CORS(app)

MAX_VAL=2
MIN_VAL=0

'''
Prior Audience Sample, to compare levels
0 = Weak
1 = Medium
2 = Strongest
'''
def _getSample():
    return random.randrange(MIN_VAL,MAX_VAL + 1)

prior = 1 #initiliaze the pryor 
jokesAndResponses = {}
jokesTold = 0
heuristics = Set()
'''
App Route Decorators for Flask interoperability
'''

@app.route("/")
def helloWorld():
    print "Inside the hello world thing in test.py"
    return "Hello, World"

@app.route("/pryor")
def returnPriorValue():
    return jsonify(pryor=prior)

@app.route("/sampleValue")
def returnTestSample():
    return jsonify(minVal=0,maxVal=2,sample=_getSample())

@app.route("/showPerformance")
def returnShowPerformance():
    if jokesTold == 0:
	return "No Current Performance Running!"
    else:
	return jsonify(currentPerformance=jokesAndResponses)

@app.route("/showHeuristics")
def returnPerformanceHeuristics():
    return jsonify(hSet=list(heuristics) )
'''
Main Function Here
'''
class heuristic(object):
    def __init__(self,t):
	self.type = t
	self.fails = 0 
	self.prob = 100 #out of a hundred percent
    def getInfo(self):
	return [self.type,self.fails,self.prob]
    def getType(self):
	return self.type
    def failSelf(self):
	print "FUCK"
	self.fails = self.fails + 1
	
	self.prob = self.prob/ (2**self.fails)

 

class performance(object):
    def __init__(self,h):
	self.allH = Set()
	for elm in h:
	    self.allH.add(heuristic(elm))

    def getInfo(self):
	print "Printing the set of heuristics:\n"
	for elm in self.allH:
	    print elm.getInfo()


    def reportFailure(self,tempH):
	for h in self.allH:
	    if h.getType() in tempH:
	    	#print "HERE IS A FAILING HEURISTIC: ", h
	    	h.failSelf()
	

if __name__=="__main__":
    g = Digraph('Unconnected Jokes', filename="unconnectedJokes.gv")
    g.attr('node',shape='circle')
    random.seed()

    #this is the sim for getting audience input for jokes
    allJokes = pickle.load(open("smallerObjects.p","rb"))

    #create set for heuristics
    for joke in allJokes:
	heuristics.add(joke[1])
	heuristics.add(joke[2])
	heuristics.add(joke[3])

       
    p = performance(heuristics)
    p.getInfo() 
    for joke in allJokes:


	#joke = [ Name,	Category, Version,  Length ]
	print "\n\nTELLING JOKE: ", joke[0]
	print joke
	g.node(joke[0])

	#Current Joke Heuristics
	tempH = []
	tempH.append(joke[1])
	tempH.append(joke[2])
	tempH.append(joke[3])
	

        #Gets Reponse after telling a joke
	jokeResp = _getSample()
        jokesTold = jokesTold + 1

	print "PRIOR (PRYOR): ", prior
	print "SIMULATED RESPONSE VAL: ", jokeResp       
	
	print "ROBOT RESPONSE:"
	if jokeResp > prior:
	    print "Whoops, that joke didnt go well!"
            binaryResponse = "BAD"
	    p.reportFailure(tempH)
	else:
	    print "The joke went well"
	    binaryResponse = "GOOD"

	p.getInfo()
	jokesAndResponses.update({joke[0]:binaryResponse})

    print "DONE WITH PERFORMANCE"
    #prints the graph, and runs the flask server 
    g.view()
    app.run()
