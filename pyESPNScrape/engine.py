from bs4 import BeautifulSoup
import requests
import lxml
from schedule_array import getGameIds
from insert_team import insertTeam, buildTeam
from sample_espn import sample_espn
from insert_game import getSummaryDateTime, getGameId, createSummarySoup, getTeamId, getSummaryLocation, buildGame, insertGame
from insert_player import buildPlayers, insertPlayers
from insert_gameStats import buildGameStats, insertGameStats

schedURL = 'http://www.espn.com/mens-college-basketball/team/schedule/_/id/120/year/2018'
gameIds = getGameIds(schedURL)
for x in range(len(gameIds)):
	url = 'http://www.espn.com/mens-college-basketball/boxscore?gameId=' + str(gameIds[x])
	#print (url)
	r = requests.get(url)

	gameSoup = BeautifulSoup(r.text, 'lxml')


	#add team info to db
	insertTeam(buildTeam(gameSoup,0,gameIds[x]))
	insertTeam(buildTeam(gameSoup,1,gameIds[x]))

	# rootAwayCSS = "div.col.column-one.gamepackage-away-wrap"
	playerArray = buildPlayers(gameSoup,gameIds[x])

	for y in range(0, len(playerArray)):
		insertPlayers(playerArray[y])

	#print(buildGame(gameSoup, url))
	insertGame(buildGame(gameSoup, url, gameIds[x]))

	gameStatsArray = buildGameStats(gameSoup, url)
	for y in range(0, len(gameStatsArray)):
		insertGameStats(gameStatsArray[y])

	print('Finished Game #' + str(x))
