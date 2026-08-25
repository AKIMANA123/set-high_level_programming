#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine and connect to database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities ordered by id, and use the state relationship
    cities = session.query(City).order_by(City.id).all()

    # Display results in the format: <city id>: <city name> -> <state name>
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()
