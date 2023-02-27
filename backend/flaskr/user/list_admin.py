from main import app,email_regex
from flask import request,jsonify
from http import HTTPStatus
import os,hashlib
from model import db

@app.route("/list/admin")
def listAdmin():
    listUser = db.execute(f"select id_user,name,username,email,gender from tbl_user where role = 'admin' ")
    y = []
    for i in listUser:
        y.append(i)
    listSelectUser = []
    for i in y:
        dictUser ={
            "id": i[0],
            "name": i[1],
            "username": i[2], 
            "email": i[3], 
            "gender": i[4]
        }
        listSelectUser.append(dictUser)
    response = {
            "data": listSelectUser,
            "message": "Success"
        }
    return jsonify(response),HTTPStatus.OK