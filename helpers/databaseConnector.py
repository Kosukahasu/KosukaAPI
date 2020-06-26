import mysql.connector
from mysql.connector import errorcode

try:
	cnx = mysql.connector.connect(
		user       = "root",
		password   = "",
		host       = "127.0.0.1",
		database   = "omthpl2020",
		autocommit = True)
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		raise Exception('Something is wrong with your username or password.')
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		raise Exception('Database does not exist.')
	else:
		raise Exception(err)
else:
	SQLd = cnx.cursor(dictionary=True, buffered=True)
	SQL = cnx.cursor(buffered=True)
if not SQL: raise Exception('Could not connect to SQL.')
