#!/usr/bin/python3
"""Contains Class and Definition of staate"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declaration import declarative_base


Base = declarative_base()

class State(Base):
    """Class that inherits from Base"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
