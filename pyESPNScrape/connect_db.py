import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'port': '8889',
  'database': 'mdstats',
  'raise_on_warnings': True,
}

def db_connector(config):
	try:
	  cnx = mysql.connector.connect(**config)
	  print("Connected.")
	  return cnx
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	  else:
		print(err)
  
  	return None

#cursor.close()
#cnx.close()

