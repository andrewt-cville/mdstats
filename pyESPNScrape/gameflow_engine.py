from bs4 import BeautifulSoup
import lxml
import ast
from sample_gameflow import sample_gameflow

player, basket = '',''

def splitBasket(sentence):
    if "made" in sentence:
        sentence = sentence.split('made')
        player = sentence[0].strip()
        basket = sentence[1].strip()
        scoreArray = [player, basket]
    else:
        scoreArray = ['End of 1st Half','Free Throw']
    return scoreArray

def qualifyScore(basketType):
    onePoint = ['Free Throw']
    twoPoints = ['Dunk', 'Layup', 'Jumper', 'Two Point Tip Shot']
    threePoints = ['Three Point Jumper']

    if basketType in onePoint:
        return '1'
    if basketType in twoPoints:
        return '2'
    if basketType in threePoints:
        return '3'

gameflowSoup = BeautifulSoup(sample_gameflow, 'lxml')

dataFlow = gameflowSoup.find("div")

dataPlays = dataFlow["data-plays"]
dataPlaysArray = ast.literal_eval(dataPlays)
#print (dataPlaysArray[0])



for d in range(0, len(dataPlaysArray)):
    x = dataPlaysArray[d]['text']
    if x.count('.') > 1:
        x = x.split('.')
        scoreArray = splitBasket(x[0])
        assisted = x[1].split('by')
        print(scoreArray[0] + ': ' + qualifyScore(scoreArray[1]) + '(' + assisted[1].strip() + ')')
    else:
        scoreArray = splitBasket(x)
        print(scoreArray[0] + ': ' + qualifyScore(scoreArray[1]))
    #player = dataPlaysArray[d]['text'].split('made')
    #print (x)
    #print(dataPlaysArray[d]['text'])
    #print(dataPlaysArray[d]['text'].count('.'))

#print(dataFlow.attrs)

#print(dataFlow.text)
