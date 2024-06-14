
from flask import Flask, Blueprint, request, redirect, render_template
from markupsafe import escape

bp = Blueprint('hello', __name__, url_prefix='/')

@bp.route('/hello/')
@bp.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)




