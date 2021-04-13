import requests
import routes
import json
from random import randint

class TestCupom:

    def test_get_cupons_response_code_200(self):
        response = requests.get(routes.CUPONS)
        assert response.status_code == 200
    
    def test_post_cupons_response_code_200(self):
        payload = {'tag':f'Cupom{randint(1, 100)}', 'discount': 5, 'type': '%' }
        headers = {'content-type': 'application/json'}
        response = requests.post(routes.CUPONS, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200

    

