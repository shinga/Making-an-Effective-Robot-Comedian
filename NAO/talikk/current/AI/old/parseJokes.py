import pickle


lst = []
lineCounter=0
tmpObj=[]
for line in open("jokesFile.txt","r"):
    lineCounter+=1
    if lineCounter is 1:
        tmpObj.append(line)
    elif lineCounter is 2:
        tmpObj.append(line)
    elif lineCounter is 5:
        tmpObj.append(line)
    elif lineCounter is 6:
        tmpObj.append(line)
    elif lineCounter is 9:
        lst.append(tmpObj)
        tmpObj = []
        lineCounter = 0


pickle.dump(lst,open("smallerObjects.p", "wb"))
