from flask import Flask
from flask_cors import CORS
import cPickle as pickle
from main_ai import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
    print "Hello, World"

temp = pickle.load(open("jokePickle.p","rb"))
for joke in temp:
    print "\nHere is a joke"
    joke._printInfo()
