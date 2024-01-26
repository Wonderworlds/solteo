from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()


class Database:
    """database class to handle database creation and session management"""

    session = None

    def __init__(self, uri):
        engine = db.create_engine(uri)
        if not database_exists(engine.url):
            print("Creating database")
            create_database(engine.url)
        else:
            print("Database already exists")
        print("Connect to Database")
        self.session = db.session
        self.conn = engine.connect()

    def __del__(self):
        print("Closing database connection")
