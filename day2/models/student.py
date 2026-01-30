from sqlalchemy import Column, Integer, String
from .base import Base

"""
Class name or __tablename__ defines the name of table
a Class is equlant to Table, Datamembers or Variables are equlant to Column of table
objects of a Class are considered as rows or records of a table
"""

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    course = Column(String)

# class StudentCourses:
#     __tablename__ = "student_courses"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     age = Column(Integer)
#     course = Column(String)
