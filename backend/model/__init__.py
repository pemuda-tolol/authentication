import db_settings 
from .base import db

 
db.bind(**db_settings.db_params)
db.generate_mapping(create_tables=True)




