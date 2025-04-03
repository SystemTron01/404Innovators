from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from sqlalchemy.ext.mutable import MutableList

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    skills = Column(String)
    availability = Column(String)
    current_tasks = Column(MutableList.as_mutable(JSON), default=[])  # Corrected
    capacity = Column(Integer)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    required_skills = Column(String)
    required_people = Column(Integer)
    assigned_to = Column(MutableList.as_mutable(JSON), default=[])  # Corrected
    status = Column(String)
