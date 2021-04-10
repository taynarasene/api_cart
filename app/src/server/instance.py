from flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api( self.app,
            version='1.0',
            title="Teste",
            doc="/docs" 
        )
    
    def run(self,):
        self.app.run(host='0.0.0.0', port=8080)

server = Server()