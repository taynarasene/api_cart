from flask import Flask, request
from src.server.instance import server
from src.models.cupons import Cupom, cupons_schema, cupom_schema
from flask.json import jsonify

app, db = server.app, server.db

class Cupons():

    @app.route('/cupons')
    def index_cupom():
        cupons = Cupom.query.all()
        result = cupons_schema.dump(cupons)
        return jsonify({'Cupons': result })
    
    @app.route('/cupons/<int:id>', methods=['GET'])
    def index_cupom_by_id(id):
        cupom = Cupom.query.get(id)
        result = cupom_schema.dump(cupom)
        if result:
            return jsonify({'Cupom': result })
        else:
            return jsonify({'code': 404, 'message': f"Cupom id {id} não encontrado"}), 404

    @app.route('/cupons', methods=['POST'])
    def create_cupom():
        try:
            cupom = Cupom(
                request.json['tag'],
                request.json['discount'],
                request.json['type']
            )

            if not Cupons.has_tag(cupom.tag):
                db.session.add(cupom)
                db.session.commit()
                result = cupom_schema.dump(cupom)
                return jsonify(result)
            else:
                return jsonify({'code': 400, 'message': f"Cupom {cupom.tag} já Existe"}), 400
        except:
            return jsonify({'code': 400, 'message': 'Verifique os dados enviados'}), 400
    
    @app.route('/cupons/<int:id>', methods=['PUT'])
    def update_cupom(id):
        cupom = Cupom.query.get_or_404(id)

        if 'tag' in request.json:
             if not Cupons.has_tag(request.json['tag']):
                cupom.tag = request.json['tag']
             else:
                 return jsonify({'code': 400, 'message': f"Cupom {request.json['tag']} já Existe"}), 400
        if 'discount' in request.json:
            cupom.discount = request.json['discount']
        if 'type' in request.json:
            cupom.type = request.json['type']

        db.session.commit()
        result = cupom_schema.dump(cupom)
        return jsonify(result)
    
    @app.route('/cupons/<int:id>', methods=['DELETE'])
    def delete_cupom(id):
        cupom = Cupom.query.get(id)
        if cupom:
            db.session.delete(cupom)
            db.session.commit()
            return jsonify({'id': id, 'message': 'deleted'}), 200
        return jsonify({'code': 404, 'message': f"Cupom id {id} não encontrado"}), 404

    def has_tag(tag):
        has_cupom = Cupom.query.filter_by(tag = tag).first()
        if has_cupom:
            return True
        return False

cupons = Cupons()