from graphviz import Digraph
import cPickle as pickle
from main_ai import *
from flask import Flask
from flask_cors import CORS
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
    #from main_ai import *
    temp = pickle.load(open("jokePickle.p","rb"))
    for joke in temp:
        g.node(joke[0]._getName())
        print "\nHere is a joke"
        joke[0]._printInfo()
    '''
    This is the range of the energy value: [0,32768]
    Start of a joke, start sampling the energy of the microphones
    When joke is finished, take the mean energy. If the newest sample is lower 
    than the mean, the currrent joke heuristics are a failure, and the discount
    factor is applied to the probability of global heuristics.

    The sample is avg'd with the current shows average energy
    After this computation, the robot needs to decide which joke to do. It computes the probability of success of each joke, and adds them to a priority queue
    It pops the top joke off and performs it
    '''
    app.run()
    g.view()
