from flask import Flask
from flask_restplus import Api, Resource, abort
from src.server.instance import server

app, api = server.app, server.api

cupons_db =   [ 
                    { 
                        "Cupons" :[
                            {
                                "id":1, 
                                "tag": "Desconto", 
                                "discount": "5", 
                                "type":"%",
                                "enabled_products": [1,2,3]
                            }
                        ]   
                    }
                ]

@api.route('/cupons')
class Cupons(Resource):

    def get(self,):
        return cupons_db
    
    def post(self,):
        try:
            response = api.payload
            if Cupons.cupom_id_validate(self,response['id']) and Cupons.cupom_tag_validate(self,response['tag']):
                cupons_db[0]['Cupons'].append(response)
                return {"id": response['id'], "message": "Sucesso", "code": "200"}, 200
            return abort(500)
        except:
            return abort(500, message='Solicitação inválida, verifique o payload enviado')

    def cupom_id_validate(self,cupon_id):
        cupons = cupons_db[0]['Cupons']
        for item in cupons:
            if item['id'] == cupon_id :  
                return False 
        return True
    
    def cupom_tag_validate(self,cupon_tag):
        cupons = cupons_db[0]['Cupons']
        for item in cupons:
            if item['tag'] == cupon_tag :  
                return False 
        return True


cupons = Cupons()
