from app.extensions import db


class UktModel(db.Model):
    __tablename__ = 'tb_ukt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'))
    fakultas_id = db.Column(db.Integer, db.ForeignKey('tb_fakultas.id'))
    jurusan_id = db.Column(db.Integer, db.ForeignKey('tb_jurusan.id'))
    semester_id = db.Column(db.Integer, db.ForeignKey('tb_semester.id'))
    ipk = db.Column(db.String(32), nullable=False)
    status_mhs = db.Column(db.Enum('aktif', 'cuti'), nullable=False)
    organisasi_mhs = db.Column(db.Enum('ada', 'pasif'), nullable=False)
    jml_tanggungan = db.Column(db.Integer, nullable=False)
    jml_pendapatan = db.Column(db.String(16), nullable=False)
    bantuan = db.Column(db.Enum('terima', 'tidak terima'))

    def __repr__(self):
        return 'Id : {}, user_id {} '.format(self.id, self.user_id)
