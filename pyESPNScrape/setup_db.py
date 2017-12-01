import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': '8889',
  'raise_on_warnings': True,
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


#create tables

DB_NAME = 'mdstats'

TABLES = {}

TABLES['b_games'] = (
    "CREATE TABLE `games` ("
    "  `keygame` int(20) NOT NULL,"
    "  `keyhometeam` int(20) NOT NULL,"
    "  `keyawayteam` int(20) NOT NULL,"
    "  `gametime` datetime NOT NULL,"
	"  `gamelocation` integer(5) NOT NULL,"
    "  PRIMARY KEY (`keygame`), KEY `keyhometeam` (`keyhometeam`),"
    "  KEY `keyawayteam` (`keyawayteam`),"
    "  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`keyhometeam`) "
    "     REFERENCES `teams` (`keyteam`) ON DELETE CASCADE,"
    "  CONSTRAINT `games_ibfk_2` FOREIGN KEY (`keyawayteam`) "
    "     REFERENCES `teams` (`keyteam`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['a_teams'] = (
    "CREATE TABLE `teams` ("
    "  `keyteam` int(20) NOT NULL,"
    "  `teamshort` varchar(5) NOT NULL,"
    "  `teamlong` varchar(200) NOT NULL,"
    "  PRIMARY KEY (`keyteam`)"
    ") ENGINE=InnoDB")

TABLES['c_players'] = (
    "CREATE TABLE `players` ("
    "  `keyplayer` int(20) NOT NULL,"
    "  `keyteam` int(20) NOT NULL,"
    "  `name` varchar(200) NOT NULL,"
    "  `position` varchar(10) NOT NULL,"
    "  PRIMARY KEY (`keyplayer`), KEY `keyteam` (`keyteam`),"
    "  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`keyteam`) "
    "     REFERENCES `teams` (`keyteam`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['j_gamestats'] = (
    "CREATE TABLE `gamestats` ("
    "  `keygamestats` int(10) NOT NULL AUTO_INCREMENT,"
    "  `keygame` int(20) NOT NULL,"
    "  `keyplayer` int(20) NOT NULL,"
    "  `minutes` int(3) NOT NULL,"
    "  `fgm` int(3) NOT NULL,"
    "  `fga` int(3) NOT NULL,"
    "  `threem` int(3) NOT NULL,"
    "  `threea` int(3) NOT NULL,"
    "  `ftm` int(3) NOT NULL,"
    "  `fta` int(3) NOT NULL,"
    "  `oreb` int(3) NOT NULL,"
    "  `dreb` int(3) NOT NULL,"
    "  `reb` int(3) NOT NULL,"
    "  `ast` int(3) NOT NULL,"
    "  `stl` int(3) NOT NULL,"
    "  `blk` int(3) NOT NULL,"
    "  `turnover` int(3) NOT NULL,"
    "  `pf` int(3) NOT NULL,"
    "  `points` int(3) NOT NULL,"
    "  PRIMARY KEY (`keygamestats`), KEY `keygame` (`keygame`),"
    "  KEY `keyplayer` (`keyplayer`),"
    "  CONSTRAINT `gamestats_ibfk_1` FOREIGN KEY (`keygame`) "
    "     REFERENCES `games` (`keygame`) ON DELETE CASCADE,"
    "  CONSTRAINT `gamestats_ibfk_2` FOREIGN KEY (`keyplayer`) "
    "     REFERENCES `players` (`keyplayer`) ON DELETE CASCADE,"
    "  INDEX `unique_gamestats1` (`keygame`, `keyplayer`) "
    ") ENGINE=InnoDB")
# need to figure out the proper syntax for the create
# StoredProc['playergamestats'] = (
# 	"CREATE PROCEDURE `mdstats`.`GetPlayerGameStats`(IN keyplayer_val INT)"
# 	"BEGIN "
# 	"select a.keygame, b.teamshort, a.points, d.gametime "
# 	"from gamestats a "
# 	"left join games d on a.Keygame = d.keygame "
# 	" left join teams b on (d.Keyhometeam = b.KeyTeam and d.Keyhometeam <> 120) or (d.keyawayteam = b.KeyTeam and d.keyawayteam <>120) "
# 	"where a.keyplayer = (keyplayer_val) order by d.gametime asc"
# 	"END")
  
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name))
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

