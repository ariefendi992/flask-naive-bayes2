import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from app.models.user_model import UserModel
from app.extensions import db

users = Blueprint('users', __name__, template_folder='../templates/pages/user')


@users.route('/users')
def indexUser():
    # x = add_months(datetime.datetime(*[int(item) for item in x.split('-')]), 1).strftime("%Y-%m-%d")

    obj_date = "2022-02-12"
    format = "%Y-%m-%d"
    toDate = datetime.datetime.strptime(obj_date, format)
    print(toDate)
    print(type(toDate))
    query = UserModel.query.all()
    for i in query:
        print(type(i.created_at))

    return render_template('user-page.html', query=query)


@users.route('/add-user', methods=['GET', 'POST'])
def addUser():
    if request.method == 'POST':
        nim = request.form.get('nim')
        nama = request.form.get('nama')
        tgl_lahir = request.form.get('tgl')
        alamat = request.form.get('alamat')
        jk = request.form.get('jenis_kelamin')
        password = request.form.get('password')

        save = UserModel(nim=nim, nama=nama, tgl_lahir=tgl_lahir,
                         alamat=alamat, jenis_kelamin=jk)
        save.setPassword(password)
        db.session.add(save)
        db.session.commit()
        return redirect(url_for('users.indexUser'))
    else:
        return render_template('add-user-page.html')
