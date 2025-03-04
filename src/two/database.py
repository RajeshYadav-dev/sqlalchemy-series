from sqlalchemy import create_engine,String,Integer,Column
from sqlalchemy.orm import declarative_base
import os

os.makedirs("src/two/data", exist_ok=True)
# Set the database path
DATABASE_URL = "sqlite:///./src/two/data/database.db"

db_url = "sql"
engine = create_engine(url=DATABASE_URL)

Base = declarative_base()

class User(Base):
  __tablename__ = "users"
  
  uid = Column(Integer,nullable=False,primary_key=True,index=True)
  name= Column(String,nullable=False,index=True)
  email = Column(String,nullable=False,index=True)

Base.metadata.create_all(bind=engine)










