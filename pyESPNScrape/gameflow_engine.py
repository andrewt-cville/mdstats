from bs4 import BeautifulSoup
import lxml
import ast
from sample_gameflow import sample_gameflow


gameflowSoup = BeautifulSoup(sample_gameflow, 'lxml')

dataFlow = gameflowSoup.find("div")

dataPlays = dataFlow["data-plays"]
dataPlaysArray = ast.literal_eval(dataPlays)
print (dataPlaysArray[0])

for d in range(0, len(dataPlaysArray)):
    x = dataPlaysArray[d]['text']
    if x.count('.') > 1:
        play = x.split('.')
        print (play[0])
    else:
        print (x)
    #player = dataPlaysArray[d]['text'].split('made')
    #print (x)
    #print(dataPlaysArray[d]['text'])
    #print(dataPlaysArray[d]['text'].count('.'))

#print(dataFlow.attrs)

#print(dataFlow.text)
