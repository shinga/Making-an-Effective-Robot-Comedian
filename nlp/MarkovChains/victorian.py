import nltk
import markovify

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

  print "Generating Chains"
  texteroni = markovify.Text(cleanBook('./theDunwichHorror.txt'))

  book2 = markovify.Text(cleanBook('./theShunnedHouse.txt'))


  # COMBINE THE BOOKS
  
  print "Combining books"
  allText = markovify.combine([texteroni,book2])

  print "Here are 5 randomly generated sentences:"  
  for i in range(5):
    print allText.make_sentence()
    print '\n'


  print "Here are 5 random sentences no more than 140 characters:"

  for i in range(5):
    print allText.make_short_sentence(140)

