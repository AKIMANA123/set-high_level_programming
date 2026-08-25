#!/usr/bin/python3
"""Creates the State 'California' with the City 'San Francisco'"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


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

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State "California"
    california = State(name="California")

    # Create City "San Francisco" and link it to California
    san_francisco = City(name="San Francisco", state=california)

    # Add objects to session
    session.add(california)
    session.add(san_francisco)

    # Commit to database
    session.commit()

    # Close session
    session.close()
