from connect_db import db_connector, config
import mysql.connector
from mysql.connector import errorcode
	
def create_team(conn, team):
	"""
	Create a new project into the projects table
	:param conn:
	:param project:
	:return: project id
	"""
	sql = (" INSERT IGNORE teams(keyteam,teamshort,teamlong)"
			 " VALUES(%s,%s,%s) ")
	cur = conn.cursor()
	try:
		cur.execute(sql, team)
		conn.commit()
		cur.close()
		conn.close()
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
	
	return cur.lastrowid
	
def insertTeam(team):
 
    # create a database connection
    conn = db_connector(config)
    if conn:
        # create a new project
        team_id = create_team(conn, team)
        
def buildTeam(gameSoup,home):
 	if home == 0:
 		classVar = "away"
 	else:
 		classVar = "home"
 		
	teamIdTag = gameSoup.find("div", class_="team " + classVar)
	teamIdLinkTag = teamIdTag.find("a", class_="team-name")
	teamId = int(filter(str.isdigit, teamIdLinkTag["href"]))
	teamNames = (teamIdLinkTag.find("span", class_="long-name")).contents \
		+ (teamIdLinkTag.find("span", class_="short-name")).contents \
		+ (teamIdLinkTag.find("span", class_="abbrev")).contents

	teamArray = (teamId, str(teamNames[2]), str(teamNames[0]) + " " + str(teamNames[1]))
	return teamArray


