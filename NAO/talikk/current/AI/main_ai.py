from graphviz import Digraph
import time
import os.path
import cPickle as pickle


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
class joke(object):
    def __init__(self,_name=None,_topic=None,_length=None,_version=None,_forcedID=None,_joketext=None):
        if _name is None:
            self.name = "--missing name--" 
        else:
            self.name = _name

        #e.x. "Romance","Aging","Self Depreciation"
        if _topic is None:
            self.topic = "--missing topic--"
        else:
            self.topic = _topic

        #approximate time to tell joke (in minutes)
        if _length is None:
            self.length=-1
        else:
            self.length = _length #approximate time to tell joke

        if _joketext is None:
            self.joketext = "--insert funny joke here--"
        else:
            self.joketext = _joketext #String that humans can read that tell the joke

        #ID for behavior, and to link robot to their human versions 
        if _forcedID is not None:
            self.id = _forcedID

        if _version is not None:
            self.version = _version

    def _printInfo(self):

        print self.name
        print self.topic
        print self.length
        print self.joketext

        if self.id is not None:
            print self.id

        if self.version is not None:
            print self.version

    def _getName(self):
        return self.name

def getUserInput():
    userWords = raw_input()
    if userWords is 'q':
        return False
    else:
        return userWords

if __name__=="__main__":
    g = Digraph('Jokes',filename='jokeset.gv')

    print "Here is where you can add jokes."
    print "type 'q' to exit\n\n"

    qList = []
    qList.append("Name of the joke?") #0
    qList.append("Topic of the joke?") #1
    qList.append("Length of Joke?") #2
    qList.append("Version (Human or Robot)?:") #3
    qList.append("ForceID (if you dont know what this is, type 'no')") #4
    qList.append("Briefly ruin this joke: ") #5

    jokeObjs=[]
    done = False
    while not done:
        #get responses for the questions in qList
        respList = []
        for question in qList:
            print question
            tempInput = getUserInput()
            if tempInput is 'no':
                break
            if tempInput is not False:
                respList.append(tempInput)
            else:
                done = True
                break

        if len(respList) == len(qList):
            print "Here is the joke being appended:"
            print respList
     
            jokeObjs.append(joke(respList[0],respList[1],respList[2],respList[3],respList[4],respList[5]))
        else:
            print "Joke was terminated during entry, not appending this one"



    #Done adding nodes, time to append these jokes to the joke graph
    #filestring = time.strftime("%Y%m%d--%H:%M:%S") + ".p"
    filestring = "jokePickle.p"

    if os.path.exists(filestring):
        previousPickle = pickle.load(open(filestring,"rb") )
        previousPickle = jokeObjs + previousPickle
        pickle.dump(previousPickle,open(filestring,"wb"))
    else:
        pickle.dump(jokeObjs,open(filestring,"wb" ))


    

    #g.view()

    print "Here is the filename:"
    print filestring
