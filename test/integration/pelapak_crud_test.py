import json
from test import app, client, cache, create_token, reset_database

class TestPelapakCrud():
    var = 0
    reset_database()

    def test_Pelapak_valid_input_post_name(self, client):
        token = create_token()
        data = {
            'nama_pelapak':'raden',
            'idktp_pelapak':'33276487264211',
            'user_name':'mahar',
            'alamat_pelapak':'jombang',
            'contact_pelapak':'082283511672',
            'kelamin_pelapak':'Perempuan',
            'email_pelapak':'panji@alterra.id',
            'password_pelapak':'agh765vx765',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.post('/pelapak', data=json.dumps(data),
                        # headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        TestPelapakCrud.var = res_json['id_pelapak']
        assert res.status_code == 200
    
    def test_Pelapak_invalid_post_name(self, client):
        token = create_token()
        data = {
            'nama_pelapak':'raden',
            'idktp_pelapak':'33276487264211',
            'user_name':'mahar',
            'alamat_pelapak':'jombang',
            'contact_pelapak':'082283511672',
            'kelamin_pelapak':'Perempuan',
            'email_pelapak':'panji@alterra.id',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.post('/pelapak', data=json.dumps(data),
                        # headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 400
    

    def test_Pelapak_valid_input_put(self, client):
        token = create_token()
        data = {
            'nama_pelapak':'Bambang',
            'idktp_pelapak':'4298472974',
            'user_name' : 'Mahar',
            'alamat_pelapak' : 'jombang',
            'contact_pelapak' : '082283511672',
            'kelamin_pelapak' : 'pria',
            'email_pelapak' : 'raden@gmail.com',
            'password_pelapak' : 'agh765',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.put('/pelapak/'+str(TestPelapakCrud.var), data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_Pelapak_valid_option(self, client):
        res = client.options('/pelapak', content_type='application/json')

        assert res.status_code == 200

    def test_Pelapak_valid_patch(self, client):
        res = client.patch('/pelapak', content_type='application/json')

        assert res.status_code == 501

    def test_Pelapak_invalid_input_put(self, client):
        token = create_token()
        data = {
            'nama_pelapak':'manga',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.put('/pelapak1/'+str(TestPelapakCrud.var), data=json.dumps(data),
                        # headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def test_Pelapak_getlist(self, client): # client dr init test
        token = create_token()
        res = client.get('/pelapak/listpelapak',
                            # headers={'Authorization':'Bearer ' + token},
                            content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Pelapak_get_invalid_id_token(self, client):
        res = client.get('/pelapak/'+str(TestPelapakCrud.var),
                        headers={'Authorization':'Bearer abc'})
        
        res_json = json.loads(res.data)
        assert res.status_code == 422
    
    def test_Pelapak_get_valid_id_token(self, client):
        token = create_token()
        res = client.get('/pelapak/'+str(TestPelapakCrud.var),
                        headers={'Authorization':'Bearer ' + token})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Pelapak_delete_token(self, client):
        token = create_token()
        res = client.delete('/pelapak/'+str(TestPelapakCrud.var),
                        headers={'Authorization':'Bearer ' + token})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Pelapak_invalid_delete_token(self, client):
        token = create_token()
        res = client.delete('/pelapak/500',
                        headers={'Authorization':'Bearer ' + token})
        
        res_json = json.loads(res.data)
        assert res.status_code == 404
    
    def test_Pelapak_invalid_getlist(self, client): # client dr init test
        token = create_token()
        res = client.get('/pelapak/list1',
                            # headers={'Authorization':'Bearer ' + token},
                            content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 401