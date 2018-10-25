from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getAPIKeys_database_setup import Base, Appkeys

app = Flask(__name__)

# absolute path used
engine = create_engine('sqlite:////vagrant/myAPIkeys.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

def getAPIKey(provider, app):
    appkey = session.query(Appkeys).filter_by(provider=provider, app=app).one()
    return appkey    
    