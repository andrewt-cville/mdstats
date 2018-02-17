from db_config import config
from db_functions import create_database, createFKIndexes, createTables
from db_definitions import INDEX, TABLES, DB_NAME
import mysql.connector
from mysql.connector import errorcode

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

cursor = cnx.cursor()

create_database(cursor, DB_NAME)

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

createTables(cnx, TABLES, cursor)
createFKIndexes(cnx, INDEX, cursor)
cursor.close()
cnx.close()
