#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    """Get the arguments from the command line"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    """Create engine that connects to MySQL server at localhost:3306"""
    engine = create_engine("""mysql+mysqldb://{}:{}@localhost:3306/{}"""
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    """Create a configured "Session" class"""
    Session = sessionmaker(bind=engine)
    """Create a session"""
    session = Session()
    """Create a new state object"""
    new_state = State(name="California")
    """Create a new city object linked to the new state"""
    new_city = City(name="San Francisco", state=new_state)
    """Add the new state and city to the session"""
    session.add(new_state)
    session.add(new_city)
    """Commit the changes to the database"""
    session.commit()
    """Close the session"""
    session.close()
