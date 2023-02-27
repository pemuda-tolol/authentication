import db_settings
from . import author, book, book_category, borrowed_book, borrowed_detail, publisher
from .base import db
from . import user




db.bind(**db_settings.db_params)
db.generate_mapping(create_tables=True)




