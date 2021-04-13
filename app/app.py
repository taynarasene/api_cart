from src.server.instance import server

app= server.app

from src.controllers.products import products
from src.controllers.cupons import cupons
from src.controllers.carts import carts


server.run()