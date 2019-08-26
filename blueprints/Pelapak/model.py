from blueprints import db
from flask_restful import fields

class Pelapaks(db.Model):
    __tablename__ = "pelapak"
    id_pelapak = db.Column(db.Integer, primary_key = True)
    nama_pelapak = db.Column(db.String(255), nullable = False)
    idktp_pelapak = db.Column(db.String(255), nullable = False)
    user_name = db.Column(db.String(255), nullable = False)
    alamat_pelapak = db.Column(db.String(255), nullable = False)
    contact_pelapak = db.Column(db.String(100), nullable = False)
    kelamin_pelapak = db.Column(db.String(30), nullable = False)
    email_pelapak = db.Column(db.String(30), nullable = False)
    password_pelapak = db.Column(db.String(30), nullable = False)
    status = db.Column(db.Boolean, nullable = False)

    response_fields = {
        'id_pelapak' : fields.Integer,
        'nama_pelapak' : fields.String,
        'idktp_pelapak' : fields.String,
        'user_name' : fields.String,
        'alamat_pelapak' : fields.String,
        'contact_pelapak' : fields.String,
        'kelamin_pelapak' : fields.String,
        'email_pelapak' : fields.String,
        'password_pelapak' : fields.String,
        'status' : fields.Boolean
    }

    jwt_response_fields = {
        'id_pelapak' : fields.Integer,
        'nama_pelapak' : fields.String,
        'user_name' : fields.String,
        'alamat_pelapak' : fields.String,
        'contact_pelapak' : fields.String,
        'email_pelapak' : fields.String,
        'status' : fields.Boolean
    }

    def __init__(self, nama_pelapak, idktp_pelapak, user_name, alamat_pelapak, contact_pelapak, kelamin_pelapak, email_pelapak, password_pelapak, status):
        self.nama_pelapak = nama_pelapak
        self.idktp_pelapak = idktp_pelapak
        self.user_name = user_name
        self.alamat_pelapak = alamat_pelapak
        self.contact_pelapak = contact_pelapak
        self.kelamin_pelapak = kelamin_pelapak
        self.email_pelapak = email_pelapak
        self.password_pelapak = password_pelapak
        self.status = status
    
    def __repr__(self):
        return '<User %r>' % self.id_pelapak
