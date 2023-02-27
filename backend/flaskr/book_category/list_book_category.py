from main import app,email_regex
from flask import request,jsonify
from http import HTTPStatus
import os,hashlib
from model import db

@app.route('/list/book/category')
def listBookCategory():
    try:
        listBookCategory = db.select(f"select *from tbl_book_category")
        listSelectBookCategory = []
        for i in listBookCategory:
            dictBookCategory ={
                "id": i[0],
                "category": i[1],
            }
            listSelectBookCategory.append(dictBookCategory)
        response = {
            "data": listSelectBookCategory,
            "message":"Data"
        }
        return jsonify(response),HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message":"BAD GATEWAY"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY

