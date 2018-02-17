DB_NAME = 'mdstats'

TABLES = {}
INDEX = {}

TABLES['b_games'] = (
    "CREATE TABLE `games` ("
    "  `keygame` int(20) NOT NULL,"
    "  `keyhometeam` int(20) NOT NULL,"
    "  `keyawayteam` int(20) NOT NULL,"
    "  `gametime` datetime NOT NULL,"
	"  `gamelocation` integer(5) NOT NULL,"
    "  PRIMARY KEY (`keygame`)"
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
    "  PRIMARY KEY (`keyplayer`)"
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
    "  PRIMARY KEY (`keygamestats`)"
    ") ENGINE=InnoDB")

INDEX['games'] = (
    "ALTER TABLE `games`"
    "ADD KEY `keyhometeam` (`keyhometeam`),"
    "ADD KEY `keyawayteam` (`keyawayteam`),"
    "ADD CONSTRAINT `games_ibfk_1` FOREIGN KEY (`keyhometeam`) "
    "   REFERENCES `teams` (`keyteam`) ON DELETE CASCADE,"
    "ADD CONSTRAINT `games_ibfk_2` FOREIGN KEY (`keyawayteam`) "
    "   REFERENCES `teams` (`keyteam`) ON DELETE CASCADE,"
    "ADD INDEX unique_games1 (keygame);")

INDEX['gamestats'] = (
    "ALTER TABLE `gamestats`"
    "ADD KEY `keygame` (`keygame`),"
    "ADD KEY `keyplayer` (`keyplayer`),"
    "ADD CONSTRAINT `gamestats_ibfk_1` FOREIGN KEY (`keygame`) "
    "   REFERENCES `games` (`keygame`) ON DELETE CASCADE,"
    "ADD CONSTRAINT `gamestats_ibfk_2` FOREIGN KEY (`keyplayer`) "
    "   REFERENCES `players` (`keyplayer`) ON DELETE CASCADE,"
    "ADD INDEX unique_gamestats1 (keygame,keyplayer);")

INDEX['players'] = (
    "ALTER TABLE `players`"
    "ADD KEY `keyteam` (`keyteam`),"
    "ADD CONSTRAINT `players_ibfk_1` FOREIGN KEY (`keyteam`) "
    "   REFERENCES `teams` (`keyteam`) ON DELETE CASCADE,"
    "ADD INDEX unique_players1 (keyplayer,keyteam);")

INDEX['teams'] = (
    "ALTER TABLE `teams`"
    "ADD INDEX unique_teams (keyteam);")
