# models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Activity(Base):
    __tablename__ = 'Activities'
    activity_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    total_hours = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    deleted_at = Column(DateTime, nullable=True)

class Student(Base):
    __tablename__ = 'Students'
    student_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    major = Column(String(50), nullable=False)
    semester = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    complementary_credits = Column(Integer, default=0)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    deleted_at = Column(DateTime, nullable=True)

class Teacher(Base):
    __tablename__ = 'Teachers'
    teacher_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    activity_id = Column(Integer, ForeignKey('Activities.activity_id'), nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    deleted_at = Column(DateTime, nullable=True)

class InProgress(Base):
    __tablename__ = 'In_Progress'
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('Students.student_id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('Teachers.teacher_id'), nullable=False)
    day_of_week = Column(String(20), nullable=False)
    schedule = Column(String(50), nullable=False)
    hours_completed = Column(Integer, nullable=False)
    hours_pending = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    deleted_at = Column(DateTime, nullable=True)
