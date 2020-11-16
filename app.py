import os
import signal
import json
from flask import Flask
from src.database import SQLConnector
from flask_restplus import Api, Resource, fields

flask_app = Flask(__name__)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")

name_space = app.namespace('main', description='Main')

model = app.model('Name Model', 
		  {'name': fields.String(required = True, 
					 description="Name of the person", 
					 help="Name cannot be blank.")})

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

#create database connection
sqlConnector = SQLConnector.SQLConnector()

@name_space.route("/test")     
class GenerateBuzz(Resource):
	@app.doc(responses={ 200: 'OK'})
	def get(self):
		#execution example
		cursor = sqlConnector.execute_query("select * from APP_USER")

		page = '<html><body><h1>'
		
		#get data from database
		page += str(cursor.fetchone())
		page += '</h1></body></html>'
		return page

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=8080)
