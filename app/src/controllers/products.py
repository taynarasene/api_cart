from flask import Flask, request
from src.server.instance import server
from src.models.products import Product, products_schema, product_schema
from flask.json import jsonify

app, db = server.app, server.db

class Products():


    @app.route('/products')
    def index():
        products = Product.query.all()
        result = products_schema.dump(products)
        return jsonify({'Products': result })
    
    @app.route('/products/<int:id>', methods=['GET'])
    def get_by_id(id):
        try:
            product = Product.query.get(id)
            if product:
                result = product_schema.dump(product)
                return jsonify({'Products': result })
            return jsonify({'code': 404, 'message': f"Produto id {id} não encontrado"}), 404
        except:
            return jsonify({'code': 400, 'message': 'Verifique os dados enviados'}), 400    

    @app.route('/products', methods=['POST'])
    def create():
        try:
            product = Product(
                request.json['name'],
                request.json['price'],
                request.json['stock']
            )
            db.session.add(product)
            db.session.commit()
            result = product_schema.dump(product)
            return jsonify(result)
        except:
            return jsonify({'code': 400, 'message': 'Verifique os dados enviados'}), 400
    
    @app.route('/products/<int:id>', methods=['PUT'])
    def put(id):
        product = Product.query.get(id)
        if product:
            if 'name' in request.json:
                product.name = request.json['name']
            if 'price' in request.json:
                product.price = request.json['price']
            if 'stock' in request.json:
                product.stock = request.json['stock']

            db.session.commit()
            result = product_schema.dump(product)
            return jsonify(result)
        return jsonify({'code': 404, 'message': f"Produto id {id} não encontrado"}), 404

    @app.route('/products/<int:id>', methods=['DELETE'])
    def delete(id):
        product = Product.query.get(id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({'id': id, 'message': 'deleted'}), 200
        return jsonify({'code': 404, 'message': f"Produto id {id} não encontrado"}), 404

        

products = Products()
