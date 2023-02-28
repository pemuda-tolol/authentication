from flask import Flask,request,jsonify
import os,re,hashlib
from pony.flask import Pony
from flask_jwt_extended import jwt_manager,JWTManager,create_access_token,jwt_required,get_jwt_identity
from http import HTTPStatus
from model import db
 

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]")


app.config['UPLOAD_FOLDER'] = os.getenv("UPLOAD_FOLDER")
app.config['MAX_CONTENT_LENGHT'] = os.getenv("MAX_CONTENT_LENGHT")
app.config['ALLOWED_EXTENSIONS'] = os.getenv("ALLOWED_EXTENSION")
 
jwt = JWTManager(app)
ponyapp = Pony(app)
 


