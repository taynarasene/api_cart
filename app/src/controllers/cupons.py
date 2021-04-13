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

    @app.route('/cupons', methods=['POST'])
    def create_cupom():
        cupom = Cupom(
            request.json['tag'],
            request.json['discount'],
            request.json['type']
        )
        has_cupom = Cupom.query.filter_by(tag = cupom.tag).first()

        if not has_cupom:
            db.session.add(cupom)
            db.session.commit()
            result = cupom_schema.dump(cupom)
            return jsonify(result)
        else:
            return jsonify({'code': 400, 'message': f"Cupom {cupom.tag} já Existe"}), 400

cupons = Cupons()