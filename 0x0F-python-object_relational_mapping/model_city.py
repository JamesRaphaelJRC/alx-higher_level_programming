#!/usr/bin/python3
''' Defines a class City '''
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    ''' Represents a City class to be linked to mysql database '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", backref="cities")
