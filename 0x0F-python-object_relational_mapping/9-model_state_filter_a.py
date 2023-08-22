#!/usr/bin/python3
''' Prints the first  State object from a database '''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    if states is None:
        print('Nothing')
    else:
        for state in states:
            if 'a' in state.name:
                print('{}: {}'.format(state.id, state.name))
