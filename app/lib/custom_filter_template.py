from flask import Blueprint
import datetime

tempFilter = Blueprint('tempFilter', __name__)


@tempFilter.app_template_filter()
def idr(rupiah):
    return 'IDR {:,}'.format(int(rupiah))


@tempFilter.app_template_filter()
def angka(value):
    # angka = round(int(value))
    return '%0.2f' % value


@tempFilter.app_template_filter()
def dateFormat(value, format="%Y-%m-%d"):
    date_obj = datetime.datetime.strptime(value, format)
    return date_obj.date()


@tempFilter.app_template_filter()
def timeIndo(value, format="%d-%m-%Y"):
    return value.strftime(format)
