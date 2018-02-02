class comedian(object):
    def __init__(self):
        self.rating = 0 #self idea of audience feedback

    def transition(self,state):
        #given a state, this function will return the next appropriate state
        #TODO where do actions influence this state machine?

    def openBit(self):
        #opening bit for performance. How to establish topics?

    def sustainBit(self):
        #This state will deliver most of the scripted content
        #can leave state if the rating drops really low
    
    def closeBit(self):
        #This should shut down the set, which should have a final thought,
        # and if the opening bit mentioned that there would be a report
        # of the audience, it should happen here
        

    def getAudienceFeedback(self):
        print "What did you think?"
        print "1 is good"
        print "0 is bad"
        usrInput = raw_input(">")

        usrInput = bool(usrInput)
        if usrInput is True or usrInput is False:
            return usrInput
        else
            return -1

if __name__=='__main___':
    print "Inside of the main"
