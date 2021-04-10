import requests
import routes
import json


class TestProducts:

    def test_get_products_response_code_200(self):
        response = requests.get(routes.PRODUCTS)
        assert response.status_code == 200
    
    def test_return_products_object_list(self):
        response = requests.get(routes.PRODUCTS).json()
        assert type(response) == type([])
    
    def test_create_product(self):
        payload = {'id':'500', 'name':'Teste', 'price': 50.00, 'stock': 50 }
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.PRODUCTS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200

    def test_return_error_with_duplicated_id(self):
        payload = {'id':'1', 'name':'Teste', 'price': 50.00, 'stock': 50 }
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.PRODUCTS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 500
    

