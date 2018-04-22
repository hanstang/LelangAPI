import falcon
import json
from itemAPI import item, item_category
from userAPI import user

cors = CORS(allow_all_origins=True, allow_all_headers=True, allow_all_methods=True)
app  = falcon.API(middleware=[
  cors.middleware
])	

###################ITEM#########################
app.add_route('/item/{itemID}', item.ObjItem())
app.add_route('/item', item.ObjItem())
app.add_route('/item_category/{categoryID}',item_category.ObjItemCategory())

##################USER################################
#app.add_route('/user/{userID}', user.ObjUserProfile())
#app.add_route('/user/', user.ObjUserProfile())