from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask.json import jsonify



class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.app.debug = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JSON_SORT_KEYS'] = False
        self.app.register_error_handler(404, Server.page_not_found)

        self.db = SQLAlchemy(self.app)
        self.ma = Marshmallow(self.app)

    
    def run(self,):
        self.app.run(host='0.0.0.0', port=8080)
        self.db.create_all()


    def page_not_found(e):
        return jsonify({'code': 404, 'message': 'Solicitação Inválida'}), 404    

server = Server()