from app.extensions import db


class FakultasModel(db.Model):
    __tablename__ = 'tb_fakultas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fakultas = db.Column(db.String(64), nullable=False)
    # ukt = db.relationship('tb_ukt', backref='tb_fakultas', lazy=True)

    def __repr__(self) -> str:
        return "Fakultas>>> id : {}, fakultas : {}".format(self.id, self.fakultas)
