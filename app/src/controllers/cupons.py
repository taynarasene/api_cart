from flask import Flask, request
from src.server.instance import server
from src.models.cupons import Cupom, cupons_schema
from flask.json import jsonify

app, db = server.app, server.db

class Cupons():

    @app.route('/cupons')
    def index_cupom():
        cupons = Cupom.query.all()
        result = cupons_schema.dump(cupons)
        return jsonify({'Cupons': result })

cupons = Cupons()