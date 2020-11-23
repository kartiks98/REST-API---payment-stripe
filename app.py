from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin


from item import Create, Show
import os

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','postgres+psycopg2://postgres:1234@localhost:5432/REST API - stores & items')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'key'
api = Api(app)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


api.add_resource(Create, '/create')
api.add_resource(Show, '/show')

# app.run(port=5000,debug=True)