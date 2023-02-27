from main import app,email_regex
from flask import request,jsonify
from http import HTTPStatus
import os,hashlib
from model import db


@app.route('/list/book/publisher')
def listBookPublisher(): 
    try:
        listBookPublisher = db.select(f"select *from tbl_book_author")
        listSelectBookPublisher = []
        for i in listBookPublisher:
            dictBookPublisher ={
                "id": i[0],
                "name": i[1],
                "email": i[2],
                "address": i[3],
                "phone_number": i[4]
            }
            listSelectBookPublisher.append(dictBookPublisher)
        response = {
            "data": listSelectBookPublisher,
            "message":"Data"
        }
        return jsonify(response),HTTPStatus.OK
    except Exception as err:
        response = {
            "data": str(err),
            "message":"BAD GATEWAY"
        }
        return jsonify(response),HTTPStatus.BAD_GATEWAY