import sqlite3
from sqlite3 import Error

database = "/Users/Andrew/Desktop/pyESPNScrape/db/sqlite.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
     
    sql_create_team_table = """ CREATE TABLE IF NOT EXISTS team (
										keyteam integer PRIMARY KEY,
										teamshort varchar(3) NOT NULL,
										teamlong varchar(100) NOT NULL
                                    ); """
 
    sql_create_game_table = """CREATE TABLE IF NOT EXISTS game (
									keygame integer PRIMARY KEY,
									keyhometeam integer NOT NULL,
									keyawayteam integer NOT NULL,
									gametime datetime NOT NULL,
									gamelocation integer NOT NULL,
									FOREIGN KEY (keyhometeam) REFERENCES team (keyteam),
									FOREIGN KEY (keyawayteam) REFERENCES team (keyteam)
							);"""
    sql_create_player_table = """CREATE TABLE IF NOT EXISTS player(
									keyplayer integer PRIMARY KEY,
									keyteam integer NOT NULL,
									name varchar(200) NOT NULL,
									position varchar(2) NOT NULL,
									FOREIGN KEY (keyteam) REFERENCES team (keyteam)
							);"""
    sql_create_gameStats_table = """CREATE TABLE IF NOT EXISTS gameStats(
									keygame integer NOT NULL,
									keyplayer integer NOT NULL,
									minutes integer NOT NULL,
									fgm integer NOT NULL,
									fga integer NOT NULL,
									threem integer NOT NULL,
									threea integer NOT NULL,
									ftm integer NOT NULL,
									fta integer NOT NULL,
									oreb integer NOT NULL,
									dreb integer NOT NULL,
									reb integer NOT NULL,
									ast integer NOT NULL,
									stl integer NOT NULL,
									blk integer NOT NULL,
									turnover integer NOT NULL,
									pf integer NOT NULL,
									points integer NOT NULL,									
									FOREIGN KEY (keygame) REFERENCES game (keygame),
									FOREIGN KEY (keyplayer) REFERENCES player (keyplayer)
							);"""
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create team table
        create_table(conn, sql_create_team_table)
        # create game table
        create_table(conn, sql_create_game_table)
        # create player table
        create_table(conn, sql_create_player_table)
        # create gameStats table
        create_table(conn, sql_create_gameStats_table)
    else:
        print("Error! cannot create the database connection.")
        
if __name__ == '__main__':
    main()