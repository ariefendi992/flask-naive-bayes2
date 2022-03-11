from email.policy import default
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime


class UserModel(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nim = db.Column(db.String(64), nullable=False)
    nama = db.Column(db.String(128), nullable=False)
    tgl_lahir = db.Column(db.String(16))
    alamat = db.Column(db.String(256), nullable=False)
    jenis_kelamin = db.Column(db.Enum('laki-laki', 'perempuan'))
    password = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)
