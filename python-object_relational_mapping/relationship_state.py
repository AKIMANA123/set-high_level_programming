#!/usr/bin/python3
"""State class definition with relationship to City using SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states"""
    
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    
    # Relationship with City class
    # - backref="state" creates a 'state' attribute in City objects
    # - cascade="all, delete-orphan" ensures cities are deleted when state is deleted
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
