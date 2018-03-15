from graphviz import Digraph
import cPickle as pickle
from main_ai import *
from flask import Flask
from flask_cors import CORS
import time
import random
from main_ai import *
app = Flask(__name__)
CORS(app)



@app.route("/")
def helloWorld():
    print "Inside the hello world thing in test.py"
    return "Hello, World"


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
    temp = pickle.load(open("jokePickle.p","rb"))
    for joke in temp:
        g.node(joke[0]._getName())
        print "\nHere is a joke"
        joke[0]._printInfo()

    g.view()

app.run()
