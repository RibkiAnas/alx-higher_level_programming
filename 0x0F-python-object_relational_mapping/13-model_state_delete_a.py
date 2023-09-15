#!/usr/bin/python3
"""
Deletes all State objects with a
name containing the letter a
from the database hbtn_0e_6_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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
    """Query the database for the states with a name containing the letter a"""
    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        """Delete the state"""
        session.delete(state)
    """Commit the changes to the database"""
    session.commit()
    """Close the session"""
    session.close()
