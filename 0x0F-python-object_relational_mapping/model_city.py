#!/usr/bin/python3
"""
The class definition of a City
and an instance Base = declarative_base()
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class with id, name and state_id
    attributes of each state
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")


State.cities = relationship("City", order_by=City.id, back_populates="state")
