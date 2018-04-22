import mysql.connector
from mysql.connector import cursor


class MySQLData:
	pass
	
	conn = None
	
	def connect_to_db(self, host, uid, pwd, db):
		self.conn = mysql.connector.connect(host=host, user=uid, password=pwd, database=db)
	
	def exec_query(self, query):
		cursor = self.conn.cursor()
		cursor.execute(query)
		#result = []
		#columns = tuple([i[0] for i in cursor.description])
		
		#for row in cursor:
		#	print('row'+row)
		#	print('col'+columns)
		#	result.append(dict(zip(columns, row)))
	
		#cursor.close()
		#return result
		return cursor
	
	def disconnect_from_db(self):
		self.conn.close()
		
	def commit_from_db(self):
		self.conn.commit()