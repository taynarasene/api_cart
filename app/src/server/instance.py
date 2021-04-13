from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.app.debug = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        self.db = SQLAlchemy(self.app)
        self.ma = Marshmallow(self.app)

    
    def run(self,):
        self.app.run(host='0.0.0.0', port=8080)
        self.db.create_all()



server = Server()