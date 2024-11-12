from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base,sessionmaker
from sqlalchemy import create_engine

# Create the database engine
engine = create_engine('sqlite:///mydatabase.db')

# Create the base class for the models
Base = declarative_base()

# Define the Parent class
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship("Child", back_populates="parent")

# Define the Child class
class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parents.id'))
    parent = relationship("Parent", back_populates="children")

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a Parent instance
parent1 = Parent(name="John Doe")

# Create Child instances
child1 = Child(name="Alice")
child2 = Child(name="Bob")

# Add the children to the parent's children list
parent1.children.append(child1)
parent1.children.append(child2)

# Add the parent to the session
session.add(parent1)

# Commit the changes to the database
session.commit()

# Close the session
session.close()