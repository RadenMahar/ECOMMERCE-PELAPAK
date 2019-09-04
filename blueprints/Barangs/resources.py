import json
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from sqlalchemy import desc
from .model import Barang
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims

from . import *
from blueprints import db, app, internal_required


bp_barang = Blueprint('barang', __name__)

api = Api(bp_barang)

class EditBarang(Resource):
    def __init__(self):
        pass
    
    def options(self, barang_id = None):
        return {"status":"ok"},200
    
    def get(self, barang_id):
        Qry = Barang.query.get(barang_id)
        if Qry is not None:
            return marshal(Qry, Barang.response_fields), 200, {'Content-Type' : 'application/json'}
        return {'status' : 'NOT_FOUND'}, 404
    
    @jwt_required
    @internal_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_barang', location='json', required=True)
        parser.add_argument('tipe_barang', location='json', required=True)
        parser.add_argument('deskripsi_barang', location='json', required=True)
        parser.add_argument('harga_barang', location='json', required=True)
        parser.add_argument('tahun_barang', location='json', required=False)
        parser.add_argument('image_barang', location='json', required=True)
        args = parser.parse_args()

        #untuk mendapatkan identitas pelapak yang login
        pelapak = get_jwt_claims()

        barang = Barang(args['nama_barang'], args['tipe_barang'], args['deskripsi_barang'], args['harga_barang'], pelapak['user_name'], args['tahun_barang'], args['image_barang'])
        db.session.add(barang)
        db.session.commit()

        app.logger.debug('DEBUG : %s', barang)

        return marshal(barang, Barang.response_fields), 200, {'Content-Type' : 'application/json'}

    @jwt_required
    @internal_required
    def put(self, barang_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_barang', location='json', required=False)
        parser.add_argument('tipe_barang', location='json', required=False)
        parser.add_argument('deskripsi_barang', location='json', required=False)
        parser.add_argument('harga_barang', location='json', required=False)
        parser.add_argument('tahun_barang', location='json', required=False)
        parser.add_argument('image_barang', location='json', required=False)
        args = parser.parse_args()

        Qry = Barang.query.get(barang_id)
        if Qry is None:
            return {'status' : 'NOT_FOUND'}, 404

        if args['nama_barang'] != "":
            Qry.nama_barang = args['nama_barang']
        if args['tipe_barang'] != "":
            Qry.tipe_barang = args['tipe_barang']
        if args['deskripsi_barang'] != "":
            Qry.deskripsi_barang = args['deskripsi_barang']
        if args['harga_barang'] != "":
            Qry.harga_barang = args['harga_barang']
        if args['tahun_barang'] != "":
            Qry.tahun_barang = args['tahun_barang']
        if args['image_barang'] != "":
            Qry.image_barang = args['image_barang']
        db.session.commit()

        return "Data barang Sudah terupdate", 200
    
    def patch(self, barang_id):
        return "Not yet implemented", 501    

class DeleteBarang(Resource):

    def options(self, barang_id = None):
        return {"status":"ok"},200
        
    @jwt_required
    @internal_required
    def delete(self, barang_id):
        qry = Barang.query.get(barang_id)
        if qry is None:
            return {'status' : 'NOT_FOUND'}, 404

        db.session.delete(qry)
        db.session.commit()
        return {'Status' : 'DELETED'}, 200

class SemuaBarang(Resource):
    def __init__(self):
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type = int, location = 'args', required = False, default = 1)
        parser.add_argument('rp', type = int, location = 'args', required = False, default = 25)
        # parser.add_argument('user_name', location = 'body')
        args = parser.parse_args()

        offset = args['p']*args['rp'] - args['rp']

        qry = Barang.query

        print(qry)

        qry= qry.limit(args['rp']).offset(offset).all()
        # return marshal(qry, Barang.response_fields), 200
        list_temp = []

        for row in qry:
            print("data ku",marshal(row, Barang.response_fields))
            list_temp.append(marshal(row, Barang.response_fields))
        
        return list_temp, 200
            
class SemuaBarangPelapak(Resource):
    def __init__(self):
        pass
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type = int, location = 'args', required = False, default = 1)
        parser.add_argument('rp', type = int, location = 'args', required = False, default = 25)
        # parser.add_argument('username_pelapak', location = 'body', required = True)
        args = parser.parse_args()

        offset = args['p']*args['rp'] - args['rp']

        # pelapak = get_jwt_claims()
        # print(pelapak['user_name'])

        # qry = Barang.query.filter_by(username_pelapak=pelapak['user_name'])
        qry = Barang.query

        qry= qry.limit(args['rp']).offset(offset).all()
        list_temp = []
        for row in qry:
            list_temp.append(marshal(row, Barang.response_fields))
        
        return list_temp, 200

api.add_resource(EditBarang, '', '/<barang_id>')
api.add_resource(DeleteBarang, '', '/delete/<barang_id>')
api.add_resource(SemuaBarang, '', '/semuabarang')
api.add_resource(SemuaBarangPelapak, '', '/barangpelapak')
api.add_resource(Weather, '', '/weather')
        



        

