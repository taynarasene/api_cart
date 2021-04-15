from flask import Flask, request, json
from src.server.instance import server
from src.models.carts import Cart, carts_schema, cart_schema
from src.models.cupons import Cupom, cupons_schema, cupom_schema
from src.models.products import Product, products_schema, product_schema
from flask.json import jsonify
import code


app, db = server.app, server.db

class Carts():

    @app.route('/carts')
    def list_all_carts():
        carts = Cart.query.group_by(Cart.session_id).all()
        cart_list = []
        for cart in carts:
            obj = { "Cart": {
                "session_id": cart.session_id,
                "cupom_apply": Carts.get_cupom(cart.session_id),
                "original_value": Carts.get_total_value(cart.session_id),
                "price": Carts.get_total_apply_cupom(cart.session_id, Carts.get_total_value(cart.session_id)),
                "total_quantity": Carts.get_total_quantity(cart.session_id),
                "products": json.loads(Carts.get_cart_product(cart.session_id))
            }}
            cart_list.append(obj)

        return jsonify({'Carts': cart_list })
    
    @app.route('/cart/<string:session_id>')
    def list_cart_by_session(session_id):
        # try:
            obj = [{
                "session_id": session_id,
                "cupom_apply": Carts.get_cupom(session_id),
                "original_value": Carts.get_total_value(session_id),
                "price": Carts.get_total_apply_cupom(session_id, Carts.get_total_value(session_id)),
                "total_quantity": Carts.get_total_quantity(session_id),
                "products": json.loads(Carts.get_cart_product(session_id))
            }]
            return jsonify({'Carts': obj })
        # except:
        #     return jsonify({'code': 404, 'message': f'carrinho {session_id} não encontrado' }), 404

    @app.route('/cart/<string:session_id>', methods=['POST'])
    def created_cart(session_id):
        try:
            cupom = Cupom.query.filter_by(tag = request.args.get("cupom")).first()
            product = Product.query.get(request.json['product_id'])
            cart = Cart.query.filter_by(session_id = session_id, product_id = request.json['product_id']).first()
            if cart:
                cart.quantity = cart.quantity + request.json['quantity']
                if cupom:
                    cart.cupom_id = cupom.id
                else:
                    cart.cupon_id = None
            else:
                cart = Cart(
                    session_id,
                    request.json['product_id'],
                    request.json['quantity'],
                    cupom.id if cupom else None
                )
            
            if product and product.stock >= request.json['quantity']:
                cart = Cart.query.filter_by(session_id = session_id, product_id = request.json['product_id']).first()

                product.stock = product.stock - request.json['quantity']
                db.session.add(cart)
                db.session.add(product)
                db.session.commit()
                result = cart_schema.dump(cart)
                return jsonify({'Cart': result })
            
            if product and product.stock < request.json['quantity']:
                return jsonify({'code': 400, 'message': 'Estoque insuficiente'}), 400
            
            if not product:
                return jsonify({'code': 400, 'message': 'Produto não encontrado'}), 400

        except:
            return jsonify({'code': 400, 'message': 'Verifique os dados enviados'}), 400

    @app.route('/cart/<string:session_id>/<int:id>', methods=['DELETE'])
    def delete_product_to_cart(session_id, id):
        try:
            Cart.query.filter(Cart.session_id == session_id, Cart.product_id == id).delete()        
            db.session.commit()
            return jsonify({'id': id, 'message': 'deleted'}), 200
        except:
            db.session.rollback()
            return jsonify({'code': 404, 'message': f"Produto id {id} não encontrado"}), 404

    @app.route('/cart/<string:session_id>/<int:id>', methods=['PUT'])
    def update_product_to_cart(session_id, id):
        try:
            cart = Cart.query.filter(Cart.session_id == session_id, Cart.product_id == id).first()        
            product = Product.query.get(id)
            if cart:
                if 'quantity' in request.json:
                    if product.stock > request.json['quantity']:
                        cart.quantity = request.json['quantity']
                        db.session.commit()
                        return jsonify({'id': id, 'message': 'quantidade alterada com sucesso'}), 200
                    return jsonify({'id': 400, 'message': 'produto sem estoque'}), 400
        except:
            db.session.rollback()
            return jsonify({'code': 404, 'message': f"Produto id {id} não encontrado"}), 404

    def get_total_value(session_id):
        cart = Cart.query.filter_by(session_id = session_id)
        total = 0
        for item in cart:
            product = Product.query.get(item.product_id)
            total = total + product.price * item.quantity
        return total
    
    def get_total_apply_cupom(session_id, total):
        cupom = db.session.query(Cart.session_id, Cupom.id, Cupom.tag, Cupom.discount, Cupom.type).join(Cart, Cart.cupom_id == Cupom.id).filter(Cart.session_id == session_id).first()
        if cupom != None:
            if cupom.type == '%':
                return total - (total * (cupom.discount / 100))
            else:
                return total - cupom.discount
        return total

    def get_cart_product(session_id):
        details = db.session.query(Cart.quantity, Product.id, Product.name, Product.price).join(Product, Product.id == Cart.product_id).filter(Cart.session_id == session_id ).all()
        product_list = []
        for item in details:
            product_list.append({'product_id': item.id, 'name': item.name, 'price': round(item.price, 2), 'quantity': item.quantity })

        return json.dumps(product_list)

    def get_total_quantity(session_id):
        details = db.session.query(db.func.sum(Cart.quantity).label('total')).filter(Cart.session_id == session_id).first()
        return details.total
    
    def get_cupom(session):
        cupom = db.session.query(Cart.session_id, Cupom.id, Cupom.tag).join(Cart, Cart.cupom_id == Cupom.id).filter(Cart.session_id == session).first()
        if cupom:
            return cupom.tag
        return ''


carts = Carts()