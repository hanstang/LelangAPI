from lib import mysql_lib
import falcon
import json
import datetime

class ObjUserRating:

	#show rating based on user
	def on_get(self, req, resp, userID):
		resp.status = falcon.HTTP_200
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
		
		result = md.exec_query('select * from item where CATEGORY_ID="'+categoryID+'"')
		
		resp.set_header('Content-Type', 'application/json; charset=utf-8')
		
		items = []
		for row in result:
			items.append({'item_id':row[0],'category_id':row[1],'item_name':row[2],'item_start_price':row[3],
				'item_bid_price':row[4],'item_condition':row[5],'item_description':row[6],
				'item_start_date':self.datetimeToString(row[7]),'item_due_date':self.datetimeToString(row[8])})
		
		
		resp.body = json.dumps(items)
		result.close
		md.disconnect_from_db()

class ObjUserListRating:

	#show list rating based on user
	def on_get(self, req, resp, userID):
		resp.status = falcon.HTTP_200
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
		
		result = md.exec_query('select * from item where CATEGORY_ID="'+categoryID+'"')
		
		resp.set_header('Content-Type', 'application/json; charset=utf-8')
		
		items = []
		for row in result:
			items.append({'item_id':row[0],'category_id':row[1],'item_name':row[2],'item_start_price':row[3],
				'item_bid_price':row[4],'item_condition':row[5],'item_description':row[6],
				'item_start_date':self.datetimeToString(row[7]),'item_due_date':self.datetimeToString(row[8])})
		
		
		resp.body = json.dumps(items)
		result.close
		md.disconnect_from_db()

	