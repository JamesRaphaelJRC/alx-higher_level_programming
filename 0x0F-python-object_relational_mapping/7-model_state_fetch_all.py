#!/usr/bin/python3
''' Lists all States objects from the database 'hbtn_0e_6_usa' '''
import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()

    i = 1
    for state in states:
        print("{}: {}".format(i, state.name))
        i += 1
