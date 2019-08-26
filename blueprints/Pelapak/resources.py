import json
from flask import Blueprint
from flask_restful import Resource, Api, reqparse, marshal
from sqlalchemy import desc
from .model import Pelapaks
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims


from . import *
from blueprints import db, app, internal_required

bp_pelapak = Blueprint('pelapak', __name__)

api = Api(bp_pelapak)

class editPelapak(Resource):
    def __init__(self):
        pass
    
    def options(self, pelapak_id=None):
        return {"status":"ok"},200
    
    @jwt_required
    @internal_required
    def get(self, pelapak_id = None):
        Qry = Pelapaks.query.get(pelapak_id)
        if Qry is not None:
            return marshal(Qry, Pelapaks.response_fields), 200, {'Content-Type':'application/json'}
        return {'status' : 'NOT_FOUND'}, 404
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_pelapak', location = 'json', required=True)
        parser.add_argument('idktp_pelapak', location = 'json', required=True)
        parser.add_argument('user_name', location = 'json', required = True)
        parser.add_argument('alamat_pelapak', location = 'json', required = True)
        parser.add_argument('contact_pelapak', location = 'json', required = True)
        parser.add_argument('kelamin_pelapak', location = 'json', required = True)
        parser.add_argument('email_pelapak', location = 'json', required = True)
        parser.add_argument('password_pelapak', location = 'json', required = True)
        args = parser.parse_args()

        status = True
        pelapak = Pelapaks(args['nama_pelapak'], args['idktp_pelapak'], args['user_name'], args['alamat_pelapak'], args['contact_pelapak'], args['kelamin_pelapak'], args['email_pelapak'], args['password_pelapak'], status)

        db.session.add(pelapak)
        db.session.commit()

        app.logger.debug('DEBUG : %s', pelapak)
        return marshal(pelapak, Pelapaks.response_fields), 200, {'Content-Type':'application/json'}
    
    def delete(self, pelapak_id):
        Qry = Pelapaks.query.get(pelapak_id)
        if Qry is None:
            return {'status': 'NOT_FOUND'}, 404
        
        db.session.delete(Qry)
        db.session.commit()
        return {'Status' : 'DELETED'}, 200
    
    @jwt_required
    @internal_required
    def put(self, pelapak_id):
        parser = reqparse.RequestParser()
        parser.add_argument('nama_pelapak', location = 'json', required=False)
        parser.add_argument('idktp_pelapak', location = 'json', required=False)
        parser.add_argument('user_name', location = 'json', required = False)
        parser.add_argument('alamat_pelapak', location = 'json', required = False)
        parser.add_argument('contact_pelapak', location = 'json', required = False)
        parser.add_argument('kelamin_pelapak', location = 'json', required = False)
        parser.add_argument('email_pelapak', location = 'json', required = False)
        parser.add_argument('password_pelapak', location = 'json', required = False)
        args = parser.parse_args()

        Qry = Pelapaks.query.get(pelapak_id)
        if Qry is None:
            return {'status' : 'NOT_FOUND'}, 404
        
        if args['nama_pelapak'] != "":
            Qry.nama_pelapak = args['nama_pelapak']
        if args['idktp_pelapak'] != "":
            Qry.idktp_pelapak = args['idktp_pelapak']
        if args['user_name'] != "":
            Qry.user_name = args['user_name']
        if args['alamat_pelapak'] != "":
            Qry.alamat_pelapak = args['alamat_pelapak']
        if args['contact_pelapak'] != "":
            Qry.contact_pelapak = args['contact_pelapak']
        if args['kelamin_pelapak'] != "":
            Qry.kelamin_pelapak = args['kelamin_pelapak']
        if args['email_pelapak'] != "":
            Qry.email_pelapak = args['email_pelapak']
        if args['password_pelapak'] != "":
            Qry.password_pelapak = args['password_pelapak']
        db.session.commit()

        # return marshal(Qry, Pelapaks.jwt_response_fields), 200
        return "Data pelapak Sudah terupdate", 200

    def patch(self):
        return "Not yet implemented", 501

class ListPelapak(Resource):
    def __init__(self):
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('p', type = int, location = 'args', default = 1)
        parser.add_argument('rp', type = int, location = 'args', default = 25)
        args = parser.parse_args()

        offset = args['p']*args['rp'] - args['rp']
        Qry = Pelapaks.query

        Qry = Qry.limit(args['rp']).offset(offset).all()
        list_temp = []
        for row in Qry:
            list_temp.append(marshal(row, Pelapaks.response_fields))
        
        return list_temp, 200

api.add_resource(editPelapak, '', '/<pelapak_id>')
api.add_resource(ListPelapak, '/listpelapak')