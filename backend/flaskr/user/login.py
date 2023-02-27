from main import app,email_regex
from flask import request,jsonify
from http import HTTPStatus
import os,hashlib
from model import db
from flask_jwt_extended import create_access_token

@app.route("/auth/login/user", methods = ['POST'])
def loginUser():
    try:
        jsonBody = request.json
        hashpassword = hashlib.md5((jsonBody['password']+os.getenv("SALT_PASSWORD")).encode())
        user = db.select(f"select id_user,role from tbl_user where username = '{jsonBody['username']}' and password = '{hashpassword.hexdigest()}' ")
        if user:
            access_token = create_access_token(identity={
                "id_user": user[0][0],
                "role": user[0][1]
            })
            response ={
                "Data": access_token,
                "Message": "Login Success"
            }
            return jsonify(response),HTTPStatus.OK
        else:
            response ={
                "Data": "Bad Request",
                "Message": "Username / Password is invalid"
            }
            return jsonify(response),HTTPStatus.BAD_REQUEST
    except Exception as err:
        response ={
            "Data": str(err),
            "Message": "Bad Gateway"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY