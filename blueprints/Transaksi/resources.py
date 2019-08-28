import json
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal, inputs
from sqlalchemy import desc
from .model import Transaksi
from ..Barangs.model import Barang

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims
from blueprints import db, app, internal_required

bp_transaksi = Blueprint('transaksi', __name__)

api = Api(bp_transaksi)

class SemuaTransaksi(Resource):
    def __init__(self):
        pass
    

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type = int, location = 'args', required = False, default = 1)
        parser.add_argument('rp', type = int, location = 'args', required = False, default = 25)
        parser.add_argument('id_barang', location = 'body', required=False)
        args = parser.parse_args()
        

        offset = args['p']*args['rp'] - args['rp']

        qry = Pembeli.query

        if args['id_barang'] is not None:
            qry = qry.filter_by(id_barang=args['id_barang'])

        qry = qry.limit(args['rp']).offset(offset).all()
        list_temp = []
        for row in qry:
            list_temp.append(marshal(row, Transaksi.response_fields))
        
        return list_temp, 200
    
api.add_resource(SemuaTransaksi, '')
