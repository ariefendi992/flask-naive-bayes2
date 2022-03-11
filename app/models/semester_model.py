from app.extensions import db


class SemesterModel(db.Model):
    __tablename__ = 'tb_semester'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    semester = db.Column(db.String(64), nullable=False)
    # ukt = db.relationship('tb_ukt', backref='tb_semester', lazy=True)
