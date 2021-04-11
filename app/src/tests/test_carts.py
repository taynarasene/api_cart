import requests
import routes
import json
from random import randrange



class TestCarts:

    def test_get_carts_response_code_200(self):
        response = requests.get(routes.CARTS)
        assert response.status_code == 200
    
