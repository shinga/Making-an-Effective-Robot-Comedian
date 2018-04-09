import time
import os.path
import cPickle as pickle


def getUserInput():
    userWords = raw_input()
    if userWords is 'q':
        return False
    else:
        return userWords
def writeJokesToFile(jokeObjs, fileName ):
    with open(fileName,"a") as fd:
        for joke in jokeObjs:
            fd.write("*"*20)
            for heuristic in joke:
                fd.write(str(heuristic) + "\n")
    
if __name__=="__main__":
    print "This is the script for adding jokes"
    print "type 'q' to exit at any time\n" + '*'*20+ "\n\n"

    qList = []
    qList.append("Name of the joke?") #0
    qList.append("Topic of the joke? [Romance, Jobs, Self-depreciation, etc]") #1
    qList.append("Length of Joke?[ 1, 2, 3 ]") #2
    qList.append("Version (Human or Robot)?:") #3

    jokeObjs=[]
    done = False
    while not done:
        #get responses for the questions in qList
        respList = []
        print "\n"
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

        #if all of the questions have been answered
        if len(respList) == len(qList):
            print "Here is the joke being appended:"
            print respList
            jokeObjs.append([respList[0],respList[1],respList[2],respList[3]])
        else:
            print "Joke was terminated during entry, not appending this one"



    #appending these nodes to the list of jokes
    #filestring = time.strftime("%Y%m%d--%H:%M:%S") + ".p"
    filestring = "jokeFile.txt"

    if os.path.exists(filestring):
       writeJokesToFile(jokeObjs,filestring)
    else:
       print "File does not exist, creating" 
       writeJokesToFile(jokeObjs,filestring)

    print "Here is the filename:"
    print filestring
