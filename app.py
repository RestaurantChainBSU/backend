from flask import Flask
from src.database import SQLConnector
from flask_restplus import Api, Resource, fields
from src.api import api
from flask_cors import CORS

flask_app = Flask(__name__)
CORS(app)
api.init_app(flask_app)

if __name__ == "__main__":
    flask_app.run(host='0.0.0.0', port=8080)
