#!/usr/bin/python3
''' Prints all City objects from a database '''
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City) \
        .join(State) \
        .order_by(City.id)

    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
