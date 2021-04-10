from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

@api.route('/hello')
class Home(Resource):
    def get(self,):
        return "OK"
