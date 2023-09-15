#!/usr/bin/python3
"""
Prints all City objects
from the database hbtn_0e_14_usa.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    """Query the database for all cities, joined with states"""
    for city in session.query(City).join(State).order_by(City.id):
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    """Commit the changes to the database"""
    session.commit()
    """Close the session"""
    session.close()
