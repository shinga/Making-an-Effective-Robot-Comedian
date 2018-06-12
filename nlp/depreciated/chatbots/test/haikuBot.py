import nltk
import markovify
import progressbar
import nltk
from nltk.corpus import cmudict
'''

The Great Linford is the chatbot object that receives 
input and returns an output.

would like to see this take an input of one word, and 
return a paragraph, based off of the init response. 
speed could be faster delivery. NAO moves really 
slow, and sometimes jokes need to be fast. idk


'''
d = cmudict.dict()


class theGreatLinford(object):
    def __init__(self,settings=None):
        if settings is None: #stats are out of ten
            self.speed = 5 
            self.confidence = 5
            self.intelligence = 5
            self.santity = 5
            

    #for cadence, and small familiar words
    def countSyllables(word):
        word = word.replace('-',' ')
        filterList = [',','.','?',':']
        for pattern in filterList:
            word = word.strip( pattern )
        count = 0

        try:
            test = strd[word.lower()]

        except:
            print "This word is not in the cmu dictionary!: ",word
            return 0

        #Some words have more than one way to prounce it
        diffPronounce = len(d[word.lower()]) 
        for part in word.split(' '):
            for char in d[word.lower()][0]:
                for element in char:
                    if element[-1] in ['0','1','2']:
                        count+=1
        return count



    def getIndex(inList,inString):
        for num,row in enumerate(inList):
            if inString in row:
                return num

    def cleanBook(path):
        book = open(path,'r').read()

        rows = book.split('\n')

        startIndex = getIndex(rows,'*** START')
        endIndex = getIndex(rows,'*** END')

        rows = rows[startIndex+1:endIndex]

        text = '\n'.join([r for r in rows if r !=''])
        return text

if __name__=="__main__":

    progress = 0 #out of the max value on progress bar
    bar = progressbar.ProgressBar().start(max_value=4)

    texteroni = markovify.Text(cleanBook('./theDunwichHorror.txt'))
    book2 = markovify.Text(cleanBook('./theShunnedHouse.txt'))
    progress+=1
    bar.update(progress)



    # COMBINE THE BOOKS
    allText = markovify.combine([texteroni,book2])
    progress+=1
    bar.update(progress)


    print "Here are 3 random sentences:\n\n"
    for i in range(3):
        string = allText.make_short_sentence(70)
        print string

        '''TODO
        for word in string.split(' '):
            print "Syllables in " + str( word ) + ": " + str( countSyllables(word))
        '''
    print "\n"

    progress+=1
    bar.update(progress)

    bar.finish()
    print "All Done!"


