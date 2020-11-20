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

new_dish = api.model("new_dish",
{
 "dish_name" : fields.String(required=True, description="Dish name"),
"dish_descr" : fields.String(required=True, description="Dish description"),
     "price" : fields.Float(required=True, description="Dish price"),
"image_link" : fields.String(required=True, description="Dish image")
})

@api.route('/')
class AddDish(Resource):
    @api.doc('add_dish')
    @api.expect(new_dish)
    @api.response(code=200, description="Success")
    def post(self):
        """
        Adds new dish
        """
        json_data = request.json

        required_fields = ['dish_name', 'dish_descr', 'price', 'image_link']
        check = set(required_fields).issubset({*json_data})
        print(check)
        if not check:
            return {'reason': 'not all the fields are provided'}, 400

        query = "INSERT into DISH (dish_name, dish_descr, price, image_link) values (" + \
                "'" + json_data["dish_name"] + "'," + \
                "'" + json_data["dish_descr"] + "'," + \
                "'" + str(json_data["price"]) + "'," + \
                "'" + json_data["image_link"] + "'" + \
                ")"
        res = sql_conn.execute_insert_update(query)
        inserted_id = res.lastrowid
        return {'id': inserted_id}

@api.route("/<dish_id>")
@api.param("dish_id", "Dish Id")
class GetSpecificDish(Resource):
    @api.doc('get_dish')
    @api.response(code=200, description="Success", model=dish)
    def get(self, dish_id):
        """
        Returns specific dish
        """
        query = "SELECT * FROM DISH where id='"+str(dish_id)+"'"
        res = sql_conn.execute_query(query)
        res = list(res)

        if res:
            item = res[0]
            dish = {}
            dish["id"] = item[0]
            dish["dish_name"] = item[1]
            dish["dish_descr"] = item[2]
            dish["price"] = float(item[3])
            dish["image_link"] = item[4]
            return dish
        else:
            return []

    @api.doc('delete_dish')
    @api.response(code=200, description="Success")
    def delete(self, dish_id):
        """
        Delets specific dish
        """
        query = "DELETE FROM DISH where id='"+str(dish_id)+"'"
        res = sql_conn.execute_query(query)

    @api.doc('put_dish')
    @api.expect(new_dish)
    @api.response(code=200, description="Success")
    def post(self, dish_id):
        """
        Updates dish
        """
        json_data = request.json

        required_fields = ['dish_name', 'dish_descr', 'price', 'image_link']
        check = set(required_fields).issubset({*json_data})
        print(check)
        if not check:
            return {'reason': 'not all the fields are provided'}, 400

        query = "UPDATE DISH set " + \
                "dish_name='"+ json_data["dish_name"] + "'," + \
                "dish_descr='"+ json_data["dish_descr"] + "'," + \
                "price='"+ str(json_data["price"]) + "'," + \
                "image_link='"+ json_data["image_link"] + "' where id='"+str(dish_id)+"'"
        res = sql_conn.execute_insert_update(query)
