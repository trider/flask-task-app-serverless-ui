import datetime, json, re
from flask import Flask, Blueprint, request, redirect, render_template, session
from markupsafe import escape
from api import _utils as utils
bp = Blueprint('login', __name__, url_prefix='/')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('login.html')
   

@bp.route('/login/authenticate', methods=['POST'])
def authenticateUser():
  data = utils.getLoginData(request.form)
  user = utils.login({"email": data['email'], "password": data['password']}, False)
  session['user'] = user
  return redirect('/tasks')
	
   
   
   
   






