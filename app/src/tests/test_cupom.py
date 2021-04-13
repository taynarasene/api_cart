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
    
    def test_post_cupom_duplicated_tag(self):
        payload = {'tag':'Teste Cupom Original', 'discount': 5, 'type': '%' }
        headers = {'content-type': 'application/json'}
        response_create = requests.post(routes.CUPONS, data=json.dumps(payload), headers=headers)
        response = requests.post(f'{routes.CUPONS}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 400

    def test_put_cupom(self):
        payload_create = {'tag':f'Teste Não alterado{randint(1, 100)}', 'discount': 5, 'type': '%' }
        headers = {'content-type': 'application/json'}
        response_create = requests.post(routes.CUPONS, data=json.dumps(payload_create), headers=headers)
        cupom_id = response_create.json()['id']
        payload = {'tag':f'Teste Não alterado{randint(1, 100)} novo', 'discount': 5, 'type': '%' }
        response = requests.put(f'{routes.CUPONS}/{cupom_id}', data=json.dumps(payload), headers=headers)
        assert response.status_code == 200
    
    def test_put_cupom_duplicated_tag(self):
        payload = {'tag': f'Teste Cupom Original{randint(1, 100)}', 'discount': 5, 'type': '%' }
        headers = {'content-type': 'application/json'}
        response_create = requests.post(routes.CUPONS, data=json.dumps(payload), headers=headers)
        cupom_id = response_create.json()['id']
        cupom_tag = response_create.json()['tag']
        payload_new = {'tag': f'{cupom_tag}', 'discount': 5, 'type': '%' }
        response = requests.put(f'{routes.CUPONS}/{cupom_id}', data=json.dumps(payload_new), headers=headers)
        assert response.status_code == 400

    def test_get_cupom_by_id_response_code_200(self):
        payload = {'tag': f'Teste GET {randint(1, 100)}', 'discount': 5, 'type': '%' }
        headers = {'content-type': 'application/json'}
        response_create = requests.post(routes.CUPONS, data=json.dumps(payload), headers=headers)
        cupom_id = response_create.json()['id']
        response = requests.get(f'{routes.CUPONS}/{cupom_id}', data=json.dumps(payload_new), headers=headers)
        assert response.status_code == 200
    
    def test_get_cupom_by_id_response_code_200(self):
        response = requests.get(f'{routes.CUPONS}/0')
        assert response.status_code == 404
    

