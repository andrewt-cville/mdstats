import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': '8889',
  'raise_on_warnings': True,
  'database':'mdstats'
}

try:
  cnx = mysql.connector.connect(**config)
  print("Connected.")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

INDEX = {}

INDEX['games'] = (
    "ALTER TABLE `games`"
    "ADD INDEX unique_games1 (keygame);")

INDEX['gamestats'] = (
    "ALTER TABLE `gamestats`"
    "ADD INDEX unique_gamestats1 (keygame,keyplayer);")

INDEX['players'] = (
    "ALTER TABLE `players`"
    "ADD INDEX unique_players1 (keyplayer,keyteam);")

INDEX['teams'] = (
    "ALTER TABLE `teams`"
    "ADD INDEX unique_teams (keyteam);")
\

cursor = cnx.cursor()

for name, ddl in INDEX.items():
    try:
        print("Creating index {}: ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
