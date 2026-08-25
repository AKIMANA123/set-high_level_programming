#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and connect to database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects where name contains 'a'
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()

    # Delete each state
    for state in states_to_delete:
        session.delete(state)

    # Commit the deletion
    session.commit()

    # Close session
    session.close()
