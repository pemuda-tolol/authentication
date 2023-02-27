from pony.orm import Required,PrimaryKey,Set,Optional
from datetime import date
from .base import db

class User(db.Entity):
    _table_ = "tbl_user"
    id_user = PrimaryKey(int,auto = True)
    username = Required(str,unique = True)
    email = Required(str,unique = True)
    password = Required(str)
    name = Required(str)
    gender = Required(str)
    address = Required(str)
    city = Required(str)
    phone_number = Required(str)
    date_register = Required(date)
    role = Required(str)
    borrowedbook = Set('BorrowedBook') 