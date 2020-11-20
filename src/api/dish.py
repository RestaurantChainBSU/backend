from flask import request
from flask_restplus import Namespace, Resource, fields
from src.database.SQLConnector import SQLConnector
import json

api = Namespace("dishes", description="Dishes info part")
sql_conn = SQLConnector()

dish = api.model("dish",
{
        "id" : fields.Integer(required=True, description="Dish Id"),
 "dish_name" : fields.String(required=True, description="Dish name"),
"dish_descr" : fields.String(required=True, description="Dish description"),
     "price" : fields.Float(required=True, description="Dish price"),
"image_link" : fields.String(required=True, description="Dish image")
})

@api.route("/<rest_id>")
@api.param("rest_id", "Restaurant Id")
class Dish(Resource):
    @api.doc('get_dishes')
    @api.response(code=200, description="Success", model=[dish])
    def get(self, rest_id):
        """
        Returns list of dishes for specific restaurant
        """
        dishes_from_db = []
        query = "SELECT d.* from RESTAURANT as r inner join REST_DISH as rd " + \
			    " on r.id = rd.rest_id " + \
		        " inner join DISH as d " + \
			    " on d.id = rd.dish_id " + \
                " where r.id = " + str(rest_id)
        res = sql_conn.execute_query(query)
        res = list(res)
        if res:
            for item in res:
                dish = {}
                dish["id"] = item[0]
                dish["dish_name"] = item[1]
                dish["dish_descr"] = item[2]
                dish["price"] = float(item[3])
                dish["image_link"] = item[4]
                dishes_from_db.append(dish)
            return dishes_from_db
        else:
            return []