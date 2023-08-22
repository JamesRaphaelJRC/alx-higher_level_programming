#!/usr/bin/python3
''' Defines a State model
'''
from relationship_city import Base, City
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String


class State(Base):
    ''' Represents a state for a MySQL database
        states is set as the table name with 2 columns id and name
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
