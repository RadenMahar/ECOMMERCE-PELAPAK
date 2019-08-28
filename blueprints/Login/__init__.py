from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal
from ..Pelapak.model import Pelapaks

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt_claims

bp_login = Blueprint('login', __name__)
api = Api(bp_login)

class CreateToken(Resource):
    def __init__(self):
        pass
    
    def options(self):
        return {"status":"ok"},200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email_pelapak', location='json', required=True)
        parser.add_argument('password_pelapak', location='json', required=True)
        args = parser.parse_args()

        pelapakQry = Pelapaks.query.filter_by(email_pelapak=args['email_pelapak']).filter_by(password_pelapak=args['password_pelapak']).first()
        pelapak = marshal(pelapakQry, Pelapaks.jwt_response_fields)

        if pelapakQry is not None:
            token = create_access_token(identity=pelapak)
        else:
            return {'status': 'UNAUTHORIZED', 'message': 'invalid key or secret'}, 401

        return {'token': token,"pelapak":pelapak}, 200
    
    
    # @jwt_required
    # def post(self):
    #     claims = get_jwt_claims()
    #     return claims, 200
        

class RefreshToken(Resource):

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        token = create_access_token(identity = current_user)
        return {'token': token, 'pembeli': current_user}, 200


api.add_resource(CreateToken, '')
api.add_resource(RefreshToken, '/refresh')
