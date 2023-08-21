#!/usr/bin/python3
''' Prints the State object with name passed as argument from a database '''
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

    found = False
    for state in states:
        if sys.argv[4] == state.name:
            print('{}'.format(state.id))
            found = True
    if found is False:
        print('Not found')
