from flask import Flask,request,jsonify
from pony.flask import Pony 
from http import HTTPStatus
from flask_jwt_extended import jwt_manager,JWTManager,create_access_token,jwt_required,get_jwt_identity
import os,re,hashlib
from model import db


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]")
# app.config["JWT_ACCESS_TOKEN_EXPIRES"] = os.getenv("JWT_ACCESS_TOKEN_EXPIRES")


jwt = JWTManager(app)
Pony(app)

import flaskr.user.register as register
import flaskr.user.login as login
import flaskr.user.list_admin as list_admin
import flaskr.user.list_user as list_user
import flaskr.user.delete_user as delete_user
import flaskr.user.update_user as update_user

import flaskr.book_category.create_book_category as create_book_category
import flaskr.book_category.list_book_category as list_book_category
import flaskr.book_category.update_book_category as update_book_category
import flaskr.book_category.delete_book_category as delete_book_category

import flaskr.book_author.create_book_author as create_book_author
import flaskr.book_author.list_book_author as list_book_author

import flaskr.book_publisher.create_book_publisher as create_book_publisher
import flaskr.book_publisher.list_book_publisher as list_book_publisher




















# USER ACCESS BOOK
@app.route("/list/book")
@jwt_required()
def accessBook():
    current_user = get_jwt_identity
    _id = current_user['id_user']
    _role = current_user['role']
    if _role == "user":
        historyBook = db.select(f"select  ")

# GET IDENTITY
@app.route("/pro")
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    _id = current_user['id_user']
    _role = current_user['role']
    if _role == "user":
        response = {
            "data": "BAD REQUEST",
            "message": "YOU ARE NOT ALLOWED HERE"
        }
        return jsonify(response), HTTPStatus.BAD_REQUEST
    elif _role == "admin":
        response = {
            "data": current_user,
            "message": "ok"
        }
        return jsonify(response), HTTPStatus.OK
    else:
        response = {
            "data": "BAD REQUEST",
            "message": "BAD REQUEST"
        }
        return jsonify(response),HTTPStatus.BAD_REQUEST
    
