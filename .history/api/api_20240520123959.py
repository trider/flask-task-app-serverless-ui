from api import _utils as utils
from flask import Flask, Blueprint, request
from flask_swagger_ui import get_swaggerui_blueprint

bp = Blueprint('api', __name__, url_prefix='/api')


def getPayload(request):
    if request.method == 'GET':
        return request
    elif request.method == 'POST':
        return request.json


@bp.route('/login')
def login():
    return 'login'


@bp.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


@bp.route('/<target>/<command>/<category>', methods=['GET', 'POST'])
@bp.route('/<target>/<command>/<category>/<val>', methods=['GET', 'POST'])
def getUsers(target, command, category, val=None):
    print(target, command, category, val)
    if target == 'users':
       if request.method == 'GET':
         return utils.usersManage(command, category, val, request)
       elif request.method == 'POST':
         return utils.usersManage(command, category, val, request.json)
    elif target == 'tasks':
     if request.method == 'GET':
        return utils.tasksManage(command, category, val, request)
     elif request.method == 'POST':
        return utils.tasksManage(command, category, val, request.json)
    else:
        return 'Invalid command'
