from sqlalchemy import create_engine
import os


class DatabaseCreator:

    MYSQL_HOSTNAME = 'localhost'
    MYSQL_USER = os.environ.get('DB_USER')
    MYSQL_PASSWORD = os.environ.get('DB_PASS')

    # create connection string without database
    connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}'
    engine = create_engine(connection_string)
    connection = engine.connect()

    def __init__(self, database_name):
        self.database_name = database_name

    def create_db(self):
        DatabaseCreator.engine.execute(f'CREATE DATABASE {self.database_name};')

    def delete_db(self):
        DatabaseCreator.engine.execute(f'DROP DATABASE {self.database_name};')


DatabaseCreator('F1db').create_db()

