from sqlalchemy import ForeignKey
from app.extensions import db
from app.models.fakultas_model import FakultasModel


class JurusanModel(db.Model):
    __tablename__ = 'tb_jurusan'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jurusan = db.Column(db.String(64), nullable=False)
    id_fakultas = db.Column(db.Integer, ForeignKey(FakultasModel.id))
    # ukt = db.relationship('tb_ukt', backref='tb_jurusan', lazy=True)

    def __repr__(self) -> str:
        return 'Fakultas >> id : {}, jurusan : {},  id_fakultas : {}'.format(self.id, self.jurusan, self.id_fakultas)
