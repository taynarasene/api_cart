from flask import Flask
from flask_restplus import Api, Resource, abort
from src.server.instance import server

app, api = server.app, server.api

carts_db =   [ 
                    { 
                        "Carts" :[
                            {
                                "session_id": '1pdg45ukije4hr19vhp57ddgb2',
                                "quantity": 2,
                                "original_price": 100.00,
                                "price": 95.00,
                                "Products": [
                                    { "product_id": 1,
                                      "product_name": "vestido",
                                      "price" : 50.00,
                                      "quantity": 1
                                    },
                                    { "product_id": 1,
                                      "product_name": "blusa",
                                      "price" : 50.00,
                                      "quantity": 1
                                    },
                                ]
                            }
                        ]   
                    }
                ]

@api.route('/carts')
class Carts(Resource):

    def get(self,):
        return carts_db



carts = Carts()
