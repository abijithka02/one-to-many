from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///database.db')
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    student_id = Column(Integer, ForeignKey('students.id'))
    students = relationship("Student", back_populates="courses")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Create courses
math = Course(course_name='Maths')
english = Course(course_name='English')
science = Course(course_name='Science')

# Create students
abhi = Student(name='Abhi')
jaya = Student(name='Jaya')

# Assign courses to students
abhi.courses.append(math)
abhi.courses.append(english)
jaya.courses.append(science)

# Add students to the session
session.add_all([abhi, jaya])
session.commit()