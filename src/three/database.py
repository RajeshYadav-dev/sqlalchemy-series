from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.orm import declarative_base
import os

os.makedirs("src/three/data",exist_ok=True)

database_url = "sqlite:///./src/three/data/database.db"

engine = create_engine(url=database_url)
Base = declarative_base()

class User(Base):
  __tablename__ = "users"
  uid = Column(Integer,nullable=False,primary_key=True,index=True)
  name = Column(String,nullable=False,index=True)
  age = Column(Integer,nullable=False,index=True)

Base.metadata.create_all(bind=engine)
