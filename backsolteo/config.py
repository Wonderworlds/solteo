from dotenv import load_dotenv
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY_DB", "this-is-the-default-key")
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('POSTGRES_USER', 'postgres')}\
:{os.getenv('POSTGRES_PASSWORD', 'postgres')}\
@{os.getenv('POSTGRES_HOSTNAME', 'localhost')}\
:{os.getenv('POSTGRES_PORT', '5432')}\
/{os.getenv('POSTGRES_DB', 'solteo_db')}"
    POSTGRESQL_DB = os.getenv("POSTGRESQL_DB", "solteo_db")


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
