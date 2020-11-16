import os
import signal
import json
from flask import Flask
from buzz import generator
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

@name_space.route("/test")     
class GenerateBuzz(Resource):
	@app.doc(responses={ 200: 'OK'})
	def get(self):
	    page = '<html><body><h1>'
	    page += generator.generate_buzz()
	    page += '</h1></body></html>'
	    return page

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=5000) #change port to 8080 when deploy
