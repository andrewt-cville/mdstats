from connect_db import db_connector, config
from bs4 import BeautifulSoup
import requests
import lxml	
from insert_game import getTeamId
import mysql.connector
from mysql.connector import errorcode
	
def create_players(conn, players):
	"""
	Create a new project into the projects table
	:param conn:
	:param project:
	:return: project id
	"""
	sql = ''' INSERT IGNORE players(keyplayer,keyteam,name,position)
			  VALUES(%s,%s,%s,%s) '''
	cur = conn.cursor()
	try:
		cur.execute(sql, players)
		conn.commit()
		cur.close()
		conn.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
	
	return cur.lastrowid
	
def insertPlayers(players):
 
    # create a database connection
    conn = db_connector(config)
    if conn:
        # create a new project
        team_id = create_players(conn, players)
        
def buildPlayers(gameSoup):

 	locVar = [["away", "div.col.column-one.gamepackage-away-wrap"], ["home", "div.col.column-two.gamepackage-home-wrap"]]
 	players = []
 	for x in range(0, len(locVar)):
 		playerId = gameSoup.select(locVar[x][1] + " td.name a")
		name = gameSoup.select(locVar[x][1] + " td.name a span.abbr")
		position = gameSoup.select(locVar[x][1] + " td.name span.position")
		teamId = getTeamId(locVar[x][0], gameSoup)
		for y in range(0, len(playerId)):
			#bookmark - need to get the teamid above and then iterate and create a list for each player
			players.append([int(filter(str.isdigit,playerId[y].get('href'))), teamId, str(name[y].string), str(position[y].string)])
	return players


