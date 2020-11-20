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

new_restaurant = api.model("new_restaurant",
{
 "rest_name" : fields.String(required=True, description="Restaurant name"),
"rest_descr" : fields.String(required=True, description="Restaurant description"),
   "address" : fields.String(required=True, description="Restaurant address"),
  "latitude" : fields.Float(required=True, description="Restaurant latitude"),
 "longitude" : fields.Float(required=True, description="Restaurant longitude"),
"image_link" : fields.String(required=True, description="Restaurant image")
})

dish = api.model("dish",
{
        "id" : fields.Integer(required=True, description="Dish Id"),
 "dish_name" : fields.String(required=True, description="Dish name"),
"dish_descr" : fields.String(required=True, description="Dish description"),
     "price" : fields.Float(required=True, description="Dish price"),
"image_link" : fields.String(required=True, description="Dish image")
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

    @api.doc('add_restaurant')
    @api.expect(new_restaurant)
    @api.response(code=200, description="Success")
    def post(self):
        """
        Adds new restaurant
        """
        json_data = request.json

        required_fields = ['rest_name', 'rest_descr', 'address', 'latitude', 'longitude', 'image_link']
        check = set(required_fields).issubset({*json_data})
        print(check)
        if not check:
            return {'reason': 'not all the fields are provided'}, 400

        query = "INSERT into RESTAURANT (rest_name, rest_descr, address, latitude, longitude, image_link) values (" + \
                "'" + json_data["rest_name"] + "'," + \
                "'" + json_data["rest_descr"] + "'," + \
                "'" + json_data["address"] + "'," + \
                "'" + str(json_data["latitude"]) + "'," + \
                "'" + str(json_data["longitude"]) + "'," + \
                "'" + json_data["image_link"] + "'" + \
                ")"
        res = sql_conn.execute_insert_update(query)
        inserted_id = res.lastrowid
        return {'id': inserted_id}

    

@api.route('/<id>')
@api.param('id', 'Restaurant id')
class GetSpecificRestaurant(Resource):
    @api.doc('get_restaurant')
    @api.response(code=200, description="Success", model=restaurant)
    def get(self, id):
        """
        Returns specific restaurant
        """
        query = "SELECT * FROM RESTAURANT where id='"+str(id)+"'"
        res = sql_conn.execute_query(query)
        res = list(res)

        if res:
            item = res[0]
            restaurant = {}
            restaurant["id"] = item[0]
            restaurant["rest_name"] = item[1]
            restaurant["rest_descr"] = item[2]
            restaurant["address"] = item[3]
            restaurant["latitude"] = float(item[4])
            restaurant["longitude"] = float(item[5])
            restaurant["image_link"] = item[6]
            return restaurant
        else:
            return []

    @api.doc('delete_restaurant')
    @api.response(code=200, description="Success")
    def delete(self, id):
        """
        Delets specific restaurant
        """
        query = "DELETE FROM RESTAURANT where id='"+str(id)+"'"
        res = sql_conn.execute_query(query)

    @api.doc('put_restaurant')
    @api.expect(new_restaurant)
    @api.response(code=200, description="Success")
    def post(self, id):
        """
        Updates restaurant
        """
        json_data = request.json

        required_fields = ['rest_name', 'rest_descr', 'address', 'latitude', 'longitude', 'image_link']
        check = set(required_fields).issubset({*json_data})
        print(check)
        if not check:
            return {'reason': 'not all the fields are provided'}, 400

        query = "UPDATE RESTAURANT set " + \
                "rest_name='"+ json_data["rest_name"] + "'," + \
                "rest_descr='"+ json_data["rest_descr"] + "'," + \
                "address='"+ json_data["address"] + "'," + \
                "latitude='"+ str(json_data["latitude"]) + "'," + \
                "longitude='"+ str(json_data["longitude"]) + "'," + \
                "image_link='"+ json_data["image_link"] + "' where id='"+str(id)+"'"
        res = sql_conn.execute_insert_update(query)

@api.route("/<rest_id>/dishes")
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
