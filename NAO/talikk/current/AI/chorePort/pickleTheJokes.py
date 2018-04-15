import pickle


lst = []
lineCounter=0
tmpObj=[]
for line in open("jokeFile.txt","r"):
    lineCounter+=1
    if lineCounter is 1:
        tmpObj.append(line)
    elif lineCounter is 2:
        tmpObj.append(line)
    elif lineCounter is 3:
        tmpObj.append(line)
    elif lineCounter is 4:
        tmpObj.append(line)
        tmpObj = []
        lineCounter = 0


pickle.dump(lst,open("smallerObjects.p", "wb"))
