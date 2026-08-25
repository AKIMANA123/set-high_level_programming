#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

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

    # Get the first State object ordered by id
    # Using first() avoids fetching all states
    state = session.query(State).order_by(State.id).first()

    # Display result
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")

    # Close session
    session.close()
