import cPickle as pickle
from jokeObj import joke

pList = []
fd = open("funnyJokes.p","wb")
#print "Running"
j = joke(name="DialUpHuman",ID="#0001",referenceSpace="Crowd",topic="Dating",human=True,CW=False)
j.addHeuristic("Testing")
pList.append(j)
#print j.getHeuristics()

j = joke(name="DialUpRobot",ID="#0002",referenceSpace="Shared",topic="Dating",human=True,CW=False)
pList.append(j)

j = joke(name="BreakALegRobot",ID="#0003",referenceSpace="Robot",topic="Jobs",human=True,CW=False)
pList.append(j)

j = joke(name="CarbonDatingRobot",ID="#0004",referenceSpace="Shared",topic="Dating",human=True,CW=False)
pList.append(j)


pickle.dump(pList,fd)
fd.close()

    


    

    
