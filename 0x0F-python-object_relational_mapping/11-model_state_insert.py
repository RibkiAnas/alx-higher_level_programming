#!/usr/bin/python3
"""
adds the State object “Louisiana”
to the database hbtn_0e_6_usa.
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
    engine = create_engine("""mysql+mysqldb://{}:{}@127.0.0.1:3307/{}"""
                           .format(username, password, database))
    Base.metadata.create_all(engine)
    """Create a configured "Session" class"""
    Session = sessionmaker(bind=engine)
    """Create a session"""
    session = Session()
    """Create a new State object"""
    newState = State(name="Louisiana")
    """Add a new State to the session"""
    session.add(newState)
    """Commit the changes to the session"""
    session.commit()
    print(newState.id)
    """Close the session"""
    session.close()
