from flask import request
from flask_restplus import Namespace, Resource, fields
from src.database.SQLConnector import SQLConnector
import json

api = Namespace("restaurants", description="Restaurants info part")
sql_conn = SQLConnector()

restaurant = api.model("restaurant",
{
        "id" : fields.Integer(required=True, description="Restaurant Id"),
 "rest_name" : fields.String(required=True, description="Restaurant name"),
"rest_descr" : fields.String(required=True, description="Restaurant description"),
   "address" : fields.String(required=True, description="Restaurant address"),
  "latitude" : fields.Float(required=True, description="Restaurant latitude"),
 "longitude" : fields.Float(required=True, description="Restaurant longitude"),
"image_link" : fields.String(required=True, description="Restaurant image")
})

@api.route('/')
class Restaurant(Resource):
    @api.doc('get_restaurants')
    @api.response(code=200, description="Success", model=[restaurant])
    def get(self):
        """
        Returns list of all restaurants
        """
        restaurants_from_db = []
        query = "SELECT id, rest_name, rest_descr, address, latitude, longitude, image_link  FROM RESTAURANT"
        res = sql_conn.execute_query(query)
        res = list(res)
        if res:
            for item in res:
                restaurant = {}
                restaurant["id"] = item[0]
                restaurant["rest_name"] = item[1]
                restaurant["rest_descr"] = item[2]
                restaurant["address"] = item[3]
                restaurant["latitude"] = float(item[4])
                restaurant["longitude"] = float(item[5])
                restaurant["image_link"] = item[6]
                restaurants_from_db.append(restaurant)
            return restaurants_from_db
        else:
            return []