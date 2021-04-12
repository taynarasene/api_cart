
from src.server.instance import server

db, ma = server.db, server.ma

class Product(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    stock = db.Column(db.Integer, unique=False, nullable=False)

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "price", "stock")
        model = Product

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)