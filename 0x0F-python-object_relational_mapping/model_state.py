#!/usr/bin/python3
''' Inherits from SQLAlchemy Base and links to the MySQL table states.
'''

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    ''' Represents a state for a MySQL database
        states is set as the table name with 2 columns id and name
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
