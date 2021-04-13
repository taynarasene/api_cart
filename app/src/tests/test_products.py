import requests
import routes
import json
from random import randrange


class TestProducts():

    def test_get_products_response_code_200(self):
        response = requests.get(routes.PRODUCTS)
        assert response.status_code == 200
    
    def test_create_product(self):
        payload = {'name':'Teste New', 'price': 50.00, 'stock': 50 }
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.PRODUCTS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200

    def test_put_product(self):
        payload_create = {'name':'Teste Não alterado', 'price': 50.00, 'stock': 50 }
        headers = {'content-type': 'application/json'}
        response_create = requests.post(routes.PRODUCTS, data=json.dumps(payload_create), headers=headers)
        product_id = response_create.json()['id']
        payload = {'name':'Teste Put', 'price': 50.00, 'stock': 50 }
        response = requests.put(f'{routes.PRODUCTS}/{product_id}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 200
    
    def test_delete_product(self):
        payload_create = {'name':'Teste Delete', 'price': 50.00, 'stock': 50 }
        headers = {'content-type': 'application/json'}
        response_create = requests.post(routes.PRODUCTS, data=json.dumps(payload_create), headers=headers)
        product_id = response_create.json()['id']
        response = requests.delete(f'{routes.PRODUCTS}/{product_id}', headers=headers)
        assert response.status_code == 200

    

