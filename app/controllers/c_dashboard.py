from flask import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__,
                      template_folder='../templates/pages')


@dashboard.route('/')
def indexDashboard():
    return render_template('dashboard.html')
