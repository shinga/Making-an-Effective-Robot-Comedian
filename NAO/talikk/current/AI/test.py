from flask import Flask
from flask_cors import CORS
from graphviz import Digraph
import cPickle as pickle
from main_ai import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
    print "Hello, World"

g = Digraph('Unconnected Jokes', filename="unconnectedJokes.gv")
g.attr('node',shape='circle')
temp = pickle.load(open("jokePickle.p","rb"))
for joke in temp:
    g.node(joke._getName())
    print "\nHere is a joke"
    joke._printInfo()

g.view()
