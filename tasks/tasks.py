
import datetime, json, re
from flask import Flask, Blueprint, request, redirect, render_template, session
from flask_modals import render_template_modal, response
from markupsafe import escape
from api import _utils as utils

tableCols = [
    'name',
    'description',
    'added',
    'updated',
    'status',
  ]

bp = Blueprint('tasks', __name__, url_prefix='/')
@bp.route('/tasks')
def getTasks():
    
    user = json.loads(session.get('user'))
    tasks = utils.tasksDataGet('tasks', user['userName'], isAPI=False)

    
    return render_template('tasks.html', tasks=json.loads(tasks), user=user, tableCols=tableCols)
  
@bp.route('/tasks/add', methods=['POST'])
def addTask():
  data = request.form
  user = json.loads(session.get('user'))
  task ={
    'name': data['name'],
    'description': data['description'],
    'user': user['userName'], # 'userName': 'admin
    'status': 'do',
  }
  print(task)
  utils.tasksManageAction('add', None, task)
  return redirect('/tasks')



@bp.route('/tasks/edit/<taskId>', methods=['POST', 'GET'])
def editTask(taskId):
  task = utils.tasksDataGet('task', taskId, isAPI=False)
  print(task)
  return render_template('edit.html', taskId=taskId, task=json.loads(task))


@bp.route('/tasks/update/<taskId>', methods=['POST', 'GET'])
def updateTask(taskId):
  data = request.form
  user = json.loads(session.get('user'))
  task ={
    'name': data['name'],
    'description': data['description'],
    'user': user['userName'],
    'taskId': taskId,
    'status': data['status'],
  }
  utils.tasksManageAction('update', taskId, task)
  return redirect('/tasks')

@bp.route('/tasks/delete/<taskId>', methods=['POST', 'GET'])
def deleteTask(taskId):
  print('deleteTask', taskId)
  utils.tasksManageAction('delete', None, {'id': taskId})
  return redirect('/tasks')




