from pony.orm import Required,PrimaryKey,Set,Optional
from .base import db
from .borrowed_book import BorrowedBook
from .book import Book

class BorrowedDetail(db.Entity):
    _table_ = "tbl_detail_borrowed_book"
    borrowed_book = PrimaryKey(BorrowedBook, column='id_book_borrowed')
    book = Required(Book, column='id_book')