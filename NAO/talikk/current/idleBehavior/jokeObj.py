class joke(object):
    def __init__(self,name,ID,referenceSpace,topic,human=False,CW=False):
        self.qualities = {"name":name,
                            "ID":ID,
                            "referenceSpace":referenceSpace,
                            "topic":topic,
                            "human":human,
                            "CW:":CW}  
        self.heuristics = []

    def addHeuristic(self,string):
        self.heuristics.append(string)


    def getHeuristics(self):
        return self.heuristics

    def getQualities(self):
        return self.qualities
        

    


    

    
