from operator import and_
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from sqlalchemy import null
from app.models.ukt_model import UktModel
from app.models.user_model import UserModel as User
from app.models.fakultas_model import FakultasModel as Fakultas
from app.models.jurusan_model import JurusanModel as Jurusan
from app.models.semester_model import SemesterModel as Semester
from app.lib.helper import listRealtionUser as RelasiUser, listRelationFakultas as RelasiFakultas, \
    listRelationJurusan as RelasiJurusan, listRelationSemester as RelasiSms
from app.extensions import db
from app.lib.get_count_ukt import bFakultas, bJurusan, totalData, totalTerima, totalTidak

ukt = Blueprint('ukt', __name__, template_folder='../templates/pages/ukt')


@ukt.route('/ukt', methods=['GET'])
def indexUkt():
    # query = UktModel.query.join(User, Fakultas, Jurusan, Semester).all()
    query = db.session.query(UktModel, User, Fakultas, Jurusan, Semester).join(
        User, Fakultas, Jurusan, Semester).all()

    # pc1 = 0
    # pcTotal = 0

    # if query:
    #     pcTotal = totalData()
    #     pc1 = totalTerima()
    #     return pcTotal, pc1
    # pc0 = totalTidak()
    # pf1 = bFakultas(1)
    # pj = bJurusan(1)

    # return render_template('ukt-page.html', query=query, pcTotal=pcTotal, pc0=pc0, pc1=pc1, pf1=pf1, pj=pj)
    return render_template('ukt-page.html', query=query)


@ ukt.route('/add-ukt', methods=['GET', 'POST'])
def addUkt():
    if request.method == 'GET':
        user = RelasiUser(User)
        fakultas = RelasiFakultas(Fakultas)
        jurusan = RelasiJurusan(Jurusan)
        semester = RelasiSms(Semester)
        return render_template('ukt-add.html', user=user, fakultas=fakultas,
                               jurusan=jurusan, semester=semester)
    else:
        nama = request.form.get('nama')
        fakultas = request.form.get('fakultas')
        jurusan = request.form.get('jurusan')
        semester = request.form.get('semester')
        ipk = request.form.get('ipk')
        status_mhs = request.form.get('status')
        organisasi_mhs = request.form.get('organisasi')
        jml_tanggungan = request.form.get('tanggungan')
        jml_pendapatan = request.form.get('pendapatan')
        bantuan = request.form.get('bantuan')

        save = UktModel(user_id=nama, fakultas_id=fakultas, jurusan_id=jurusan, semester_id=semester,
                        ipk=ipk, status_mhs=status_mhs, organisasi_mhs=organisasi_mhs,
                        jml_tanggungan=jml_tanggungan, jml_pendapatan=jml_pendapatan,
                        bantuan=bantuan)
        db.session.add(save)
        db.session.commit()
        return redirect(url_for('ukt.indexUkt'))


@ukt.route('/ukt-testing')
def testUkt():
    if request.method == 'GET':
        user = RelasiUser(User)
        fakultas = RelasiFakultas(Fakultas)
        jurusan = RelasiJurusan(Jurusan)
        semester = RelasiSms(Semester)
        return render_template('ukt-test-page.html', user=user, fakultas=fakultas,
                               jurusan=jurusan, semester=semester)


@ukt.route('/jurusan/<id>')
def arrayJurusan(id):
    # array = Jurusan.query.join(Fakultas).all()
    array = db.session.query(Jurusan, Fakultas).join(
        Fakultas).filter_by(id=id).all()

    data = []
    for i, x in array:
        obj = {}
        obj['id'] = i.id
        obj['jurusan'] = i.jurusan
        obj['id_fakultas'] = x.fakultas
        data.append(obj)

    # jurusan = RelasiJurusan(Jurusan)

    return jsonify({'fakultas_id': data})
