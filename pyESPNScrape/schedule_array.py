from bs4 import BeautifulSoup
import requests
import lxml

def getGameIds (url):
#url = 'http://www.espn.com/mens-college-basketball/team/schedule/_/id/120'
	r = requests.get(url)
	print(r.status_code)

	gameSoup = BeautifulSoup(r.text, 'lxml')

	scheduleGrid = gameSoup.find_all('li', class_='score')

	gameIds = []
	for x in gameSoup.select('li.score a'):
		gameIds.append(int(filter(str.isdigit, x.get('href'))))
	
	return gameIds
#scheduleLinks = scheduleGrid.find_all('a', 
