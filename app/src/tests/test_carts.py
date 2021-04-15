import requests
import routes
import json
from random import randrange



class TestCarts:

    def test_create_cart_return_code_200(self):
        session_id = "sessao"
        payload = {'product_id' : 1, 'quantity' : 1 }
        headers = {'content-type': 'application/json'}
        response = requests.post(f'{routes.CARTS}/{session_id}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 200  
    
    def test_create_cart_with_cupom_return_code_200(self):
        session_id = "sessao"
        cupom = "Teste"
        payload = {'product_id' : 1, 'quantity' : 1 }
        headers = {'content-type': 'application/json'}
        response = requests.post(f'{routes.CARTS}/{session_id}?{cupom}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 200 

    def test_create_cart_with_invalid_product_return_code_400(self):
        session_id = "sessao"
        cupom = "Teste"
        payload = {'product_id' : 0, 'quantity' : 1 }
        headers = {'content-type': 'application/json'}
        response = requests.post(f'{routes.CARTS}/{session_id}?{cupom}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 400  
    
    def test_create_cart_with_invalid_qualtity_return_code_400(self):
        session_id = "sessao"
        cupom = "Teste"
        payload = {'product_id' : 1, 'quantity' : 100000 }
        headers = {'content-type': 'application/json'}
        response = requests.post(f'{routes.CARTS}/{session_id}?{cupom}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 400  
    
    def test_create_cart_update_product_stock(self):
        product = requests.get(f'{routes.PRODUCTS}/1')
        session_id = "sessao"
        cupom = "Teste"
        payload = {'product_id' : 2, 'quantity' : 1 }
        headers = {'content-type': 'application/json'}
        response = requests.post(f'{routes.CARTS}/{session_id}?{cupom}', data=json.dumps(payload), headers=headers)
        update = requests.get(f'{routes.PRODUCTS}/1')
        assert update.json()['Products']['stock'] == (product.json()['Products']['stock'] - response.json()['Cart']['quantity']) 
    
