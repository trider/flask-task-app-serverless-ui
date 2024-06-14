import datetime, json, re
from flask import Flask, Blueprint, url_for, request, session, redirect, render_template, jsonify, json, request
from bson.objectid import ObjectId
from bson.json_util import dumps, JSONOptions, CANONICAL_JSON_OPTIONS, RELAXED_JSON_OPTIONS
from api import _mongo_db as mdb

CANONICAL_JSON_OPTIONS = JSONOptions(datetime_representation=2, json_mode=1, document_class=dict, tz_aware=True)


with open("config/config.json") as config_file:config = json.load(config_file)

taskDB = mdb.mongoDb(config["urlMongoAtlas"], "tasksDB")


def getLoginData(data):
 return {
  "email": data['email'],
  "password": data['password']
 }


def remove_oid(string):
    while True:
        pattern = re.compile('{\s*"\$oid":\s*(\"[a-z0-9]{1,}\")\s*}')
        match = re.search(pattern, string)
        if match:
            string = string.replace(match.group(0), match.group(1))
        else:
            return string
        



def usersManage(command, category, val, data):
    if command == 'login':
        return login(data)
    elif command == 'get':
        return usersDataGet(category, val)
    else:
        return 'Invalid command'
    
def login(data, isAPI=True):
    print('login', data)
    res = taskDB.queryCollectionItem('users', data)
    if res:
        res["created"] = str(res["created"])
        res["updated"] = str(res["updated"])
        res["status"] = "User Authenticated"
        res["isLoggedIn"] = True
        data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
        data = remove_oid(data)
        if isAPI: data = jsonify(json.loads(data))
        return data
        

    else:
        return {
            "status":"User Not Authenticated",
            "isLoggedIn":False
        }


def usersDataGet(category, val=None, data=None):
    if category == 'users':
        res = taskDB.queryCollection('users', {})
        for item in res:
            item["created"] = str(item["created"])
            item["updated"] = str(item["updated"])

    elif category == 'user':
        res = taskDB.queryCollectionItem('users', {'userName': val})
        res["created"] = str(res["created"])
        res["updated"] = str(res["updated"])
    data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
    data = remove_oid(data)
    return jsonify(json.loads(data))


def tasksManage(command, category, val=None, data=None):
    if command == 'get':
        return tasksDataGet(category, val)
    else:
    
        return tasksManageAction(command, val, data)


def tasksDataGet(category, val=None, data=None, isAPI=True):
    print(category, val, data)
    if category == 'tasks':
        res = taskDB.queryCollection('tasks', {'user': val})
        for item in res:
            item["added"] = str(item["added"])
            item["updated"] = str(item["updated"])
    elif category == 'task':
        res = taskDB.queryCollectionById('tasks', val)
        res["added"] = str(res["added"])
        res["updated"] = str(res["updated"])
    data = dumps(res, json_options=CANONICAL_JSON_OPTIONS)
    data = remove_oid(data)
    if isAPI: data = jsonify(json.loads(data))
    return data


def tasksManageAction(command, val, data):
    if command == 'add':
        return tasksDataAdd(data)
    elif command == 'update':
        return tasksDataUpdate(data, val)
    elif command == 'delete':
        return tasksDataDelete(data)


def tasksDataAdd(data):
 
    data['added'] = datetime.datetime.now()
    data['updated'] = datetime.datetime.now()
    id = taskDB.addDocumentToCollection("tasks", data)
    return {
        "status": "Task added",
        "id": str(id)
    }
    



def tasksDataUpdate(data, val):
    data['updated'] = datetime.datetime.now()
    taskDB.updateItemByid('tasks', val, {"$set": data})
    return {
        "status": "Task updated",
        "id": val
    }



def tasksDataDelete( data):
        taskDB.deleteItem('tasks', {'_id': ObjectId(data['id'])})
        return {
            "status": "Task deleted",
            "id": data['id']
        }
    

