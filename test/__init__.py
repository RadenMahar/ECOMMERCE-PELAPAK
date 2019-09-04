import pytest, json, logging
from flask import Flask, request
from blueprints.Pelapak.model import Pelapaks
from blueprints.Barangs.model import Barang
from blueprints import db, app 
from app import cache


def call_client(request):
    client = app.test_client()
    return client

@pytest.fixture
def client(request):
    return call_client(request)

def reset_database():

    db.drop_all()
    db.create_all()

    admin = Pelapaks("Panji", '13721983721939712', "raden","jombang","082283511672", "Pria", "maharraden@gmail.com", "agh765vx765", True)

    barang = Barang("TOYOTA X8", "TOYOTA", "MAHAL", "7200000", "raden", "2017", "ohyeah")
    # create test non-admin user

    # save users to database
    db.session.add(barang)
    db.session.add(admin)
    db.session.commit()

def create_token():
    token = cache.get('test-token')
    if token is None:
        data = {
            'email_pelapak' : 'maharraden@gmail.com',
            'password_pelapak' : 'agh765vx765'
        }
        # do request
        req = call_client(request)
        res = req.post('/login', data=json.dumps(data), content_type='application/json')

        # store response
        res_json = json.loads(res.data)

        logging.warning('RESULT : %s', res_json)
        # assert if the result is as expected
        assert res.status_code == 200

        # save token into cache
        cache.set('test_token',res_json['token'], timeout=60)

        return res_json['token']
    else:
        return token
