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

dish_ids = api.model("dish_ids",
{
        "id" : fields.Integer(required=True, description="Dish Id")
})

@api.route('/')
class Order(Resource):
    @api.doc("get_sum", responses={400: "Missed orders list"})
    @api.expect([dish_ids])
    def post(self):
        """
        Evaluates order price
        """
        json_data = request.json
        ids = []
        for dish in json_data:
            ids.append(dish["id"])
        str_ids = str(ids)[1:-1]

        query = "SELECT (SUM(price) over ()) as total_price from DISH where id in ("+str_ids+") limit 1;"
        res = sql_conn.execute_query(query)
        res = list(res)
        return {'result': float(res[0][0])}