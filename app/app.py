from src.server.instance import server

app, api = server.app, server.api

from src.controllers.products import products
from src.controllers.cupons import cupons
from src.controllers.carts import carts


server.run()
