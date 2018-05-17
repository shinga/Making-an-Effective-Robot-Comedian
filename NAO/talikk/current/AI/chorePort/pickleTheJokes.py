import pickle

print "This file formats the jokeFile.txt into a pickle file for easy reading and writing during the performance"
jokeCount=0
jokeList=[]
totalHeuristics=4
tempJoke=[]
tempHeuristicCount=0



print "Printing the lines of a file"
for line in open("jokeFile.txt","r"):
    line = str(line).replace("\n","")
    if "*" in line:
    	print line
    	jokeCount+=1
	jokeStart=True
	continue
    if jokeStart is True:
	tempJoke.append(line)
	tempHeuristicCount+=1
	if tempHeuristicCount is totalHeuristics:
		jokeList.append(tempJoke)
		tempJoke=[]
		jokeStart=False
		tempHeuristicCount=0
	
        
print "There were this many jokes in the file: ", jokeCount
pickle.dump(jokeList,open("smallerObjects.p", "wb"))
