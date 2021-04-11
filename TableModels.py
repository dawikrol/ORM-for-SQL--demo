from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as db
import os
from sqlalchemy.orm import sessionmaker


MYSQL_HOSTNAME = 'localhost'
MYSQL_USER = os.environ.get('DB_USER')
MYSQL_PASSWORD = os.environ.get('DB_PASS')
MYSQL_DATABASE = 'F1db'

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = db.create_engine(connection_string)
connection = engine.connect()
Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
my_session = session()


class Teams(Base):

    __tablename__ = 'teams'
    team_id = db.Column(db.Integer(), primary_key=True, unique=True)
    team_name = db.Column(db.Text(30), nullable=False)
    main_sponsor = db.Column(db.Text(30), nullable=False)
    engine_constructor = db.Column(db.Text(30), nullable=False)

    def __repr__(self):
        return f'{self.team_name} & {self.engine_constructor}'


class Cars(Base):

    __tablename__ = 'cars'
    car_id = db.Column(db.Integer(), primary_key=True, unique=True)
    number = db.Column(db.Integer(), nullable=False)
    team_id = db.Column(db.Integer(), db.schema.ForeignKey('teams.team_id'), nullable=False)
    Teams = relationship('Teams', backref='car')

    def __repr__(self):
        return f'Car: {self.car_id} tagged as: {self.number}'


class Drivers(Base):

    __tablename__ = 'drivers'
    driver_id = db.Column(db.Integer(), primary_key=True, unique=True)
    first_name = db.Column(db.Text(30), nullable=False)
    last_name = db.Column(db.Text(30), nullable=False)
    car_id = db.Column(db.Integer(), db.schema.ForeignKey('cars.car_id'), nullable=False)
    Cars = relationship('Cars', backref='driver')

    def __repr__(self):
        return f'Driver: {self.first_name} {self.last_name}'


Teams()
Cars()
Drivers()

Base.metadata.create_all(engine)

