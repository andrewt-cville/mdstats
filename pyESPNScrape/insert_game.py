from connect_db import db_connector, config
from bs4 import BeautifulSoup
import requests
import lxml	
import mysql.connector
from mysql.connector import errorcode

def create_game(conn, game):
	"""
	Create a new project into the projects table
	:param conn:
	:param project:
	:return: project id
	"""
	sql = ''' INSERT IGNORE games (keygame,keyhometeam,keyawayteam,gametime,gamelocation)
			  VALUES(%s,%s,%s,%s,%s) '''
	cur = conn.cursor()
	try:
		cur.execute(sql, game)
		conn.commit()
		cur.close()
		conn.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		
	return cur.lastrowid
	
def insertGame(game):
 
    # create a database connection
    conn = db_connector(config)
    if conn:
        # create a new project
        team_id = create_game(conn, game)
        
def buildGame(gameSoup,url):
 	classVar = [ "home", "away"]
 	game =[getGameId(url), getTeamId(classVar[0], gameSoup), getTeamId(classVar[1], gameSoup), getSummaryDateTime(getGameId(url)), getSummaryLocation(getGameId(url))]

	#teamArray = [teamId, teamNames[2], teamNames[0] + " " + teamNames[1]]
	return game

def createSummarySoup(gameId):
	url = 'http://www.espn.com/mens-college-basketball/game?gameId=' + str(gameId)
	r = requests.get(url)
	#print(r.status_code)
	summarySoup = BeautifulSoup(r.text, 'lxml')
	return summarySoup

def getGameId(url):
	#espn game id
	gameId = int(filter(str.isdigit,url))
	return gameId

def getTeamId(classVar, gameSoup):
	#espn team id
	teamIdTag = gameSoup.find("div", class_="team " + classVar)
	teamIdLinkTag = teamIdTag.find("a", class_="team-name")
	teamId = int(filter(str.isdigit, teamIdLinkTag["href"]))
	return teamId
	
def getSummaryDateTime(gameId):
	summarySoup = createSummarySoup(gameId)
	dateTag = summarySoup.find("div", class_="game-date-time")
	datetime = dateTag.span["data-date"]
	dtstring = datetime.split('T')
	finaldt = dtstring[1].strip('Z')
	return dtstring[0] + " " + finaldt

def getSummaryLocation(gameId):
	summarySoup = createSummarySoup(gameId)
	locationTag = summarySoup.find("div", class_="location-details")
	if (locationTag.find("li.span")):
		location = locationTag.li.span
		return int(filter(unicode.isdigit, location.contents[0].strip()))
	else:
		return 99999
	#return int(filter(str.isdigit, location.contents))
	
	
	
	
	
	
	
	
	
	
	