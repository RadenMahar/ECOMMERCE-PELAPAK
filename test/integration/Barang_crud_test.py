import json
from test import app, client, cache, create_token, reset_database
# from . import app

class TestBarangCrud():
    var = 0
    reset_database()
    def test_Barang_valid_input_post_name(self, client):
        token = create_token()
        data = {
            'nama_barang':'BMW X8',
            'tipe_barang':'BMW',
            'deskripsi_barang':'murah dan bagus',
            'harga_barang':'53000000',
            'tahun_barang':'2019',
            'image_barang':'https://carwow-uk-wp-0.imgix.net/bmw-x8-red-parked-render-lead-1.jpg?auto=format&cs=tinysrgb&fit=clip&ixlib=rb-1.1.0&q=60&w=750',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.post('/barang', data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        TestBarangCrud.var = res_json['barang_id']
        assert res.status_code == 200
    
    def test_Barang_invalid_post_name(self, client):
        token = create_token()
        data = {
            'tipe_barang':'BMW',
            'deskripsi_barang':'murah dan bagus',
            'harga_barang':'53000000',
            'tahun_barang':'2019',
            'image_barang':'https://carwow-uk-wp-0.imgix.net/bmw-x8-red-parked-render-lead-1.jpg?auto=format&cs=tinysrgb&fit=clip&ixlib=rb-1.1.0&q=60&w=750',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.post('/barang', data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 400
    

    def test_Barang_valid_input_put(self, client):
        token = create_token()
        data = {
            'nama_barang':'radio',
            'tipe_barang':'toyota',
            'deskripsi_barang':'mahal',
            'harga_barang':'240000',
            'tahun_barang':'2018',
            'image_barang':'ohyeah',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.put('/barang/'+str(TestBarangCrud.var), data=json.dumps(data),
                        headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Barang_invalid_input_put(self, client):
        token = create_token()
        data = {
            'nama_barang':'manga',
        }
        #karena post menggunakan data, sedangkan get menggunkan query_string
        res = client.put('/barang1/'+str(TestBarangCrud.var), data=json.dumps(data),
                        # headers={'Authorization':'Bearer ' + token},
                        content_type='application/json')
        
        res_json = json.loads(res.data)
        assert res.status_code == 404

    def test_Barang_getlist(self, client): # client dr init test
        token = create_token()
        res = client.get('/barang/barangpelapak',
                            # headers={'Authorization':'Bearer ' + token},
                            content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200

    def test_Barang_getlist_nonlapak(self, client): # client dr init test
        token = create_token()
        res = client.get('/barang/semuabarang',
                            content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Barang_valid_option(self, client):
        res = client.options('/barang', content_type='application/json')

        assert res.status_code == 200

    def test_Barang_getlist_nonlapak(self, client): # client dr init test
        token = create_token()
        res = client.get('/barang/semuabarang1',
                            content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404
    
    def test_Barang_get_invalid_id_token(self, client):
        res = client.get('/barang1/'+str(TestBarangCrud.var))
        
        res_json = json.loads(res.data)
        assert res.status_code == 404
    
    def test_Barang_get_valid_id_token(self, client):
        token = create_token()
        res = client.get('/barang/'+str(TestBarangCrud.var))
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Barang_delete_token(self, client):
        token = create_token()
        res = client.delete('/barang/delete/'+str(TestBarangCrud.var),
                        headers={'Authorization':'Bearer ' + token})
        
        res_json = json.loads(res.data)
        assert res.status_code == 200
    
    def test_Barang_invalid_delete_token(self, client):
        token = create_token()
        res = client.delete('/barang/500',
                        headers={'Authorization':'Bearer ' + token})
        
        res_json = json.loads(res.data)
        assert res.status_code == 405
    
    def test_Barang_invalid_getlist(self, client): # client dr init test
        token = create_token()
        res = client.get('/barang/barangpelapak1',
                            # headers={'Authorization':'Bearer ' + token},
                            content_type='application/json')

        res_json = json.loads(res.data)
        assert res.status_code == 404