import requests
import routes
import json
from random import randrange

class TestCupom:

    def test_get_cupons_response_code_200(self):
        response = requests.get(routes.CUPONS)
        assert response.status_code == 200
    

