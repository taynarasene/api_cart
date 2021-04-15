
from src.server.instance import server
from sqlalchemy import ForeignKey
from src.models.products import Product, products_schema, product_schema


db, ma = server.db, server.ma

class Cart(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(80), unique=False, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship("Product", backref="products")
    quantity = db.Column(db.Integer,  unique=False, nullable=False)
    cupom_id = db.Column(db.Integer,  unique=False, nullable=True)
  
    
    def __init__(self, session_id, product_id, quantity, cupom_id):
        self.session_id = session_id
        self.product_id = product_id
        self.quantity = quantity
        self.cupom_id = cupom_id

    def serialized(self):
        return {
            'session_id': self.session_id
        }

class Cartschema(ma.Schema):
    class Meta:
        fields = ("session_id", "quantity", "cupom_id", "products", "product_id")
        model = Cart


cart_schema = Cartschema()
carts_schema = Cartschema(many=True)
