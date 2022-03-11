from operator import and_
from app.models.ukt_model import UktModel as UM
from app.models.fakultas_model import FakultasModel as FM
from app.models.jurusan_model import JurusanModel as JM
from app.models.semester_model import SemesterModel as SM
from app.extensions import db
from sqlalchemy import case, func


def totalData():
    total = UM.query.count()
    return total


def totalTerima():
    terima = db.session.query(func.count(UM.bantuan)).filter(
        UM.bantuan == 'terima').scalar()

    return terima


def totalTidak():
    tidak = db.session.query(func.count(UM.bantuan)).filter(
        UM.bantuan == 'tidak terima').scalar()

    return tidak


def bFakultas(status):
    terima = db.session.query(func.count(UM.fakultas_id)).filter(
        UM.fakultas_id == status, UM.bantuan == 'terima').scalar()
    fTerima = terima / totalTerima()

    tidak = db.session.query(func.count(UM.fakultas_id)).filter(
        UM.fakultas_id == status, UM.bantuan == 'tidak terima').scalar()
    fTidak = tidak / totalTidak()
    return {
        'terima': fTerima,
        'tidak': fTidak
    }


def bJurusan(status):
    terima = db.session.query(func.count(UM.jurusan_id)).filter(
        UM.jurusan_id == status, UM.bantuan == 'terima').scalar()
    jTerima = terima / totalTerima()

    tidak = db.session.query(func.count(UM.jurusan_id)).filter(
        UM.jurusan_id == status, UM.bantuan == 'tidak terima').scalar()
    jTidak = terima / totalTidak()

    return {
        'terima': jTerima,
        'tidak': jTidak
    }


def bSemester(status):
    terima = db.session.query(func.count(UM.semester_id)).filter(
        UM.semester_id == status, UM.bantuan == 'terima').scalar()
    sTerima = terima / totalTerima()

    tidak = db.session.query(func.count(UM.semester_id)).filter(
        UM.semester_id == status, UM.bantuan == 'tidak terima').scalar()
    sTidak = tidak / totalTidak()

    return {
        'terima': sTerima,
        'tidak': sTidak
    }


def bIpk(status):
    ipk = ""
    if int(status) == 4.00:
        ipk = "sempurna"
    elif int(status) >= 3.00 & int(status) <= 3.50:
        ipk = "bagus"
    elif int(status) > 3.51 and int(status) < 3.00:
        ipk = "memuaskan"

    cases = case(
        (UM.ipk == 4.0, 'sempurna'),
        (and_(UM.ipk >= 3.00, UM.ipk <= 3.50), 'bagus'),
        (and_(UM.ipk > 3.51, UM.ipk < 3.00), 'memuaskan'),
        else_='')
    subQuery = db.session.query(UM.ipk, UM.bantuan)
    layak = db.session.query(func.count()).select_from_entity(
        subQuery.subquery()).filter(cases == ipk, UM.bantuan == 'terima')

    return layak
