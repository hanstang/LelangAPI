from lib import mysql_lib
import falcon
import json
import datetime

class ObjItemCategory:

	#show item data based on category
	def on_get(self, req, resp, categoryID):
		resp.status = falcon.HTTP_200
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
		
		result = md.exec_query('select item_id, category_id, item_name, item_start_price, item_bid_price, item_condition, item_description, item_start_date, item_due_date from item where CATEGORY_ID="'+categoryID+'"')
		
		resp.set_header('Content-Type', 'application/json; charset=utf-8')
		
		items = []
		for row in result:
			items.append({'item_id':row[0],'category_id':row[1],'item_name':row[2],'item_start_price':row[3],
				'item_bid_price':row[4],'item_condition':row[5],'item_description':row[6],
				'item_start_date':self.datetimeToString(row[7]),'item_due_date':self.datetimeToString(row[8])})
		
		
		resp.body = json.dumps(items)
		result.close
		md.disconnect_from_db()
		
	def stringToDateTime(self,inputan):
		#return inputan.strptime('%d/%m/%Y %H:%M:%S')
		return datetime.datetime.strptime(inputan,'%d/%m/%Y %H:%M:%S')
		
	def datetimeToString(self,inputan):
		return inputan.strftime('%d/%m/%Y %H:%M:%S')