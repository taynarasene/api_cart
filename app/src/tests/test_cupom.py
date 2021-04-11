import requests
import routes
import json
from random import randrange



class TestCupom:

    def test_get_cupons_response_code_200(self):
        response = requests.get(routes.CUPONS)
        assert response.status_code == 200
    
    def test_return_products_object_list(self):
        response = requests.get(routes.CUPONS).json()
        assert type(response) == type([])
    
    def test_create_cupom(self):
        payload = { 'id':randrange(0, 1000, 2),'tag': 'Cupom'+ str(randrange(0, 1000, 2)), 'discount': '5', 'type': '%', 'enabled_products': [1,2,3]}
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.CUPONS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200
    
    def test_create_cupom_with_duplicated_tag(self):
        payload = { 'id':randrange(0, 1000, 2),'tag': 'Cupom', 'discount': '5', 'type': '%', 'enabled_products': [1,2,3]}
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.CUPONS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 500

    def test_return_error_with_duplicated_id(self):
        payload = {'id':'1', 'name':'Teste', 'price': 50.00, 'stock': 50 }
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.PRODUCTS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 500
    

