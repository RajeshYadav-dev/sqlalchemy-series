from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
import os

os.makedirs("src/one-one/data",exist_ok=True)

database_url = "sqlite:///./src/one-one/data/database.db"

engine = create_engine(database_url,echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
  __tablename__ = "user"
  id = Column(Integer,primary_key=True)
  name = Column(String)
  age = Column(Integer)
  address = relationship("Address",back_populates="user",uselist=False)
  
  def __reps__(self):
    return f"<User:ID={self.id},Name={self.name}>"
  
class Address(Base):
  __tablename__ = "address"
  id = Column(Integer,primary_key=True)
  city = Column(String)
  user_id = Column(ForeignKey("user.id"))
  user = relationship("User",back_populates="address")  
  
  def __reps__(self):
    return f"<Address:ID={self.id},Name={self.city}>"

Base.metadata.create_all(bind=engine)  