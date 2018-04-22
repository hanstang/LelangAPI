from lib import mysql_lib
import falcon
import json
import datetime

class ObjUserProfile:

	#show user profile data
	def on_get(self, req, resp, userID):
		resp.status = falcon.HTTP_200
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
	
		result = md.exec_query('SELECT usr.user_id, usr.user_first_name, usr.user_last_name, cit.city_name, pro.province_name, usr.user_register_time FROM user usr INNER JOIN city cit ON usr.city_id=cit.city_id INNER JOIN province pro ON pro.province_id=cit.province_id WHERE user_id="'+userID+'"')

		resp.set_header('Content-Type', 'application/json; charset=utf-8')
		
		items = []
		for row in result:
			items.append({'user_id':row[0],'user_first_name':row[1],'category_last_name':row[2],'city_name':row[3],'province_name':row[4],'user_register_time':self.datetimeToString(row[5])})
		
		
		resp.body = json.dumps(items)
		result.close
		md.disconnect_from_db()
		
	#input user profile data
	def on_post(self, req, resp):
		resp.status = falcon.HTTP_200
		data = json.loads(req.stream.read())
		
		md = mysql_lib.MySQLData()
		md.connect_to_db('localhost', 'root', '', 'lelanginyuk')
		
		
		
		#result = md.exec_query('')'.format(a=data['CATEGORY_ID'],b=data['USER_ID'],c=data['ITEM_NAME'],d=data['ITEM_START_PRICE'],e=data['ITEM_BID_PRICE'],f=data['ITEM_CONDITION'],g=data['ITEM_DESCRIPTION'],h=self.stringToDateTime(data['ITEM_START_DATE']),i=self.stringToDateTime(data['ITEM_DUE_DATE'])))
		
		
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