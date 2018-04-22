from lib import mysql_lib
import falcon
import json
import datetime

class ObjItem:

	#show item data
	def on_get(self, req, resp, itemID):
		resp.status = falcon.HTTP_200
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
	
		result = md.exec_query('select ite.item_id, ite.user_id ,kat.category_id ,kat.category_name, ite.item_name, ite.item_start_price, ite.item_bid_price, ite.item_condition, ite.item_description, ite.item_start_date, ite.item_due_date from item ite inner join kategori kat on ite.category_id = kat.category_id where ite.ITEM_ID="'+itemID+'"')

		resp.set_header('Content-Type', 'application/json; charset=utf-8')
		
		items = []
		for row in result:
			items.append({'item_id':row[0],'user_id':row[1],'category_id':row[2],'category_name':row[3],'item_name':row[4],'item_start_price':row[5],
				'item_bid_price':row[6],'item_condition':row[7],'item_description':row[8],
				'item_start_date':self.datetimeToString(row[9]),'item_due_date':self.datetimeToString(row[10])})
		
		
		resp.body = json.dumps(items)
		result.close
		md.disconnect_from_db()
		
	#input item data
	def on_post(self, req, resp):
		resp.status = falcon.HTTP_200
		data = json.loads(req.stream.read())
		
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
		
		
		
		result = md.exec_query('insert into item (ITEM_ID, CATEGORY_ID, USER_ID , ITEM_NAME, ITEM_START_PRICE, ITEM_BID_PRICE, ITEM_CONDITION, ITEM_DESCRIPTION, ITEM_START_DATE, ITEM_DUE_DATE, ITEM_POST_DATE) values (REPLACE(UUID(),"-",""),"{a}","{b}","{c}",{d},"{e}","{f}","{g}","{h}","{i}",NOW())'.format(a=data['CATEGORY_ID'],b=data['USER_ID'],c=data['ITEM_NAME'],d=data['ITEM_START_PRICE'],e=data['ITEM_BID_PRICE'],f=data['ITEM_CONDITION'],g=data['ITEM_DESCRIPTION'],h=self.stringToDateTime(data['ITEM_START_DATE']),i=self.stringToDateTime(data['ITEM_DUE_DATE'])))
		
		
		output = []
		output.append({'input_row':result.rowcount})
		resp.body = json.dumps(output)
		
		result.close()
		md.commit_from_db()
		md.disconnect_from_db()
		
	def stringToDateTime(self,inputan):
		#return inputan.strptime('%d/%m/%Y %H:%M:%S')
		return datetime.datetime.strptime(inputan,'%d/%m/%Y %H:%M:%S')
		
	def datetimeToString(self,inputan):
		return inputan.strftime('%d/%m/%Y %H:%M:%S')