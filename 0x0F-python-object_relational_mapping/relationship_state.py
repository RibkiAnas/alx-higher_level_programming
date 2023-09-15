#!/usr/bin/python3
"""
The class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, MetaData, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    State class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="states")
