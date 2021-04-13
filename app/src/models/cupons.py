
from src.server.instance import server

db, ma = server.db, server.ma

class Cupom(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), unique=True, nullable=False)
    discount = db.Column(db.Float, unique=False, nullable=False)
    type = db.Column(db.Integer, unique=False, nullable=False)
    
    def __init__(self, tag, discount, type):
        self.tag = tag
        self.discount = discount
        self.type = type

class ProductSchema(ma.Schema):
    class Meta:
        fields = ("id", "tag", "discount", "type")
        model = Cupom

cupom_schema = ProductSchema()
cupons_schema = ProductSchema(many=True)