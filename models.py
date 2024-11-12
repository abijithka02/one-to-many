from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker,relationship

db_user = "sqlite:///database.db"
engine = create_engine(db_user)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)
    course = relationship("Course", back_populates='student')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    student = relationship("Student", back_populates = 'course')
    student_id = Column(Integer, ForeignKey('students.id'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# math = Course(course_name = 'maths')
# english = Course(course_name = 'english')
# bio = Course(course_name = 'bio')

# abijith = Student(name = 'abijith',age = 20)
# abhilash = Student(name = 'abhilash', age =24)

# abijith.course.append([math,english])
# abhilash.course.append([math,bio])

# session.add_all([abijith,abhilash])
# session.commit()

math = Course(course_name='maths')
english = Course(course_name='english')
bio = Course(course_name='bio')

abijith = Student(name='abijith', age=20)
abhilash = Student(name='abhilash', age=24)

abijith.course.append(math)
abijith.course.append(english)

abhilash.course.append(bio)


session.add_all([abijith, abhilash])
session.commit()
print("Successfully added data to the database!")