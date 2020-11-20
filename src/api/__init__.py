from flask_restplus import Api
from .user import api as user_ns
from .restaurant import api as restaurant_ns
from .dish import api as dish_ns
from .order import api as order_ns

api = Api(
		  version = "1.0", 
		  title = "RestaurantChainBSU", 
		  description = "VovaTheBest"
		  )

api.add_namespace(user_ns, path='/users')
api.add_namespace(restaurant_ns, path='/restaurants')
api.add_namespace(dish_ns, path='/dishes')
api.add_namespace(order_ns, path='/orders')
