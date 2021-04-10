from flask import Flask
from flask_restplus import Api, Resource, abort
from src.server.instance import server

app, api = server.app, server.api

products_db =   [ 
                    { 
                        "Products" :[
                            {"id":1, "name": "Blusa", "price": 50.00 }
                        ]   
                    }
                ]

@api.route('/products')
class Products(Resource):


        
    def get(self,):
        return products_db
    
    def post(self,):
        try:
            response = api.payload
            if Products.product_validate(self, response['id']):
                products_db[0]['Products'].append(response)
                return {"product": response['id'], "message": "Sucesso", "code": "200"}, 200
            return abort(500)
        except:
            return abort(500, message='Solicitação inválida, verifique o payload enviado')

    def product_validate(self,product_id):
        products = products_db[0]['Products']
        for item in products:
            if item['id'] == product_id :  
                return False 
        return True


products = Products()
