import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class Appkeys(Base):

    __tablename__ = 'keys'

    provider= Column(String(250), primary_key=True)
    app= Column(String(250), primary_key=True)
    key1 = Column(String(250), nullable=False)
    value1 = Column(String(250), nullable=False)
    key2 = Column(String(250), nullable=False)
    value2 = Column(String(250), nullable=False)

#####insert at the end of file######
engine = create_engine('sqlite:////vagrant/myAPIkeys.db?check_same_thread=False')
Base.metadata.create_all(engine)
