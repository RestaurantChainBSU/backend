from flask import request
from flask_restplus import Namespace, Resource, fields
from src.database.SQLConnector import SQLConnector
import json

api = Namespace("orders", description="Orders info part")
sql_conn = SQLConnector()

order = api.model("order",
{
        "id" : fields.Integer(required=True, description="Order Id"),
   "address" : fields.String(required=True, description="Order address"),
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
class Order(Resource):
    @api.doc("make_order", responses={400: "Missed orders list"})
    @api.expect([dish], validate=False)
    def post(self):
        """
        Makes new order
        """
        json_data = request.json
        address  = ""
        s = 0
        address = json_data[0]["address"]
        dish_amount = {}

        for dish in json_data[1:]:
            s += int(dish["price"])
            dish_amount[dish["id"]] = dish_amount.get(dish["id"], 0) + 1

        query = "INSERT into  `ORDER` (address, total_price, order_status) values (" + \
                "'" + address + "'," + \
                "'" + str(s) + "'," + \
                "'" + "0" + "'" + \
                ")"
        res = sql_conn.execute_insert_update(query)
        inserted_id = res.lastrowid

        for ids in dish_amount:
            query = "INSERT into ORDER_DISH (order_id, dish_id, amount) values (" + \
                "'" + str(inserted_id) + "'," + \
                "'" + str(ids) + "'," + \
                "'" + str(dish_amount[ids]) + "'" + \
                ")"
            res = sql_conn.execute_insert_update(query)

        return {'result': True}

@api.route("/<order_id>")
@api.param("order_id", "Order Id")
class GetSpecificDish(Resource):
    @api.doc('get_order')
    @api.response(code=200, description="Success", model=order)
    def get(self, order_id):
        """
        Returns specific order
        """
        query = "SELECT * FROM `ORDER` where id='"+str(order_id)+"'"
        res = sql_conn.execute_query(query)
        res = list(res)

        if res:
            item = res[0]
            order = {}
            order["id"] = item[0]
            order["address"] = item[1]
            order["total_price"] = float(item[2])
            order["order_status"] = item[3]
            return order
        else:
            return []

    @api.doc('delete_order')
    @api.response(code=200, description="Success")
    def delete(self, order_id):
        """
        Delets specific order
        """
        query = "DELETE FROM `ORDER` where id='"+str(order_id)+"'"
        res = sql_conn.execute_query(query)

