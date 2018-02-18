from bs4 import BeautifulSoup
import requests
import lxml
from insert_game import getGameId
import mysql.connector
from mysql.connector import errorcode
from connect_db import db_connector, config

def create_gameStats(conn, gameStats):
	"""
	Create a new project into the projects table
	:param conn:
	:param project:
	:return: project id
	"""
	sql = ''' INSERT IGNORE gamestats(keygame,keyplayer,minutes,fgm,fga,threem,threea,ftm, fta,oreb,dreb,reb,ast,stl,blk,turnover,pf,points)
			  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) '''
	cur = conn.cursor()
	try:
		cur.execute(sql, gameStats)
		conn.commit()
		cur.close()
		conn.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))

	return cur.lastrowid

def insertGameStats(gameStats):

    # create a database connection
    conn = db_connector(config)
    if conn:
        # create a new project
        team_id = create_gameStats(conn, gameStats)

def processStat(x):

	if (x == '--'):
		return '99'
	elif (x == '-----'):
		return '99-99'
	else:
		return(x)

def buildGameStats(gameSoup, url):
	locVar = [["away", "div.col.column-one.gamepackage-away-wrap"], ["home", "div.col.column-two.gamepackage-home-wrap"]]
	gameStats = []
	for x in range(0, len(locVar)):
		gameId = getGameId(url)
		playerId = gameSoup.select(locVar[x][1] + " td.name a")
		minutes = (gameSoup.select(locVar[x][1] + " td.min"))
		if (minutes == '--'):
			minutes = '99'
		fg = (gameSoup.select(locVar[x][1] + " td.fg"))
		three = (gameSoup.select(locVar[x][1] + " td.3pt"))
		ft = (gameSoup.select(locVar[x][1] + " td.ft"))
		oReb = (gameSoup.select(locVar[x][1] + " td.oreb"))
		dReb = (gameSoup.select(locVar[x][1] + " td.dreb"))
		reb = (gameSoup.select(locVar[x][1] + " td.reb"))
		ast = (gameSoup.select(locVar[x][1] + " td.ast"))
		stl = (gameSoup.select(locVar[x][1] + " td.stl"))
		blk = (gameSoup.select(locVar[x][1] + " td.blk"))
		to = (gameSoup.select(locVar[x][1] + " td.to"))
		pf = (gameSoup.select(locVar[x][1] + " td.pf"))
		points = (gameSoup.select(locVar[x][1] + " td.pts"))
		for y in range(0, len(playerId)):
			#bookmark - need to get the teamid above and then iterate and create a list for each player
			fgClean = processStat((fg[y].string)).split("-")
			threeClean = processStat((three[y].string)).split("-")
			ftClean = processStat((ft[y].string)).split("-")
			gameStats.append([gameId,int(''.join(filter(str.isdigit,playerId[y].get('href')))), \
				+ int(minutes[y].string) if (minutes[y].string != '--') else '99', \
				+ int(fgClean[0]), int(fgClean[1]), \
				+ int(threeClean[0]), int(threeClean[1]), int(ftClean[0]), \
				+ int(ftClean[1]), int(processStat(oReb[y].string)), int(processStat(dReb[y].string)), \
				+ int(processStat(reb[y].string)), \
				+ int(processStat(ast[y].string)), int(processStat(stl[y].string)), int(processStat(blk[y].string)), \
				+ int(processStat(to[y].string)), int(processStat(pf[y].string)), \
				+ int(processStat(points[y].string))])
	return gameStats
