from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
import os

os.makedirs("src/many-many/data",exist_ok=True)

database_url = "sqlite:///./src/many-many/data/database.db"

engine = create_engine(database_url,echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class StudentCourse(Base):
  __tablename__ = "studentcourse"
  stdcrs_id = Column(Integer,primary_key=True)
  std_id = Column("std_id",Integer,ForeignKey("student.std_id"))
  crs_id = Column("crs_id",Integer,ForeignKey("course.crs_id"))
  

class Student(Base):
  __tablename__ = "student"
  std_id = Column(Integer,primary_key=True)
  std_name = Column(String)
  std_age = Column(Integer)
  course = relationship("Course",back_populates="student",secondary="studentcourse")
  
  def __repr__(self):
    return f"<Student:(std_id={self.std_id},std_name={self.std_name})>"

class Course(Base):
  __tablename__ = "course"
  crs_id = Column(Integer,primary_key=True)
  crs_name = Column(String)
  crs_duration = Column(Integer)
  student = relationship("Student",back_populates="course",secondary="studentcourse")
  
  def __repr__(self):
    return f"<Course:(crs_id={self.crs_id},crs_name={self.crs_name})>"

Base.metadata.create_all(bind=engine)