from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base,relationship
import os

os.makedirs("src/one-many/data",exist_ok=True)

database_url = "sqlite:///./src/one-many/data/database.db"
engine = create_engine(url=database_url)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class BaseModel(Base):
  __abstract__ = True
  __allow_unmapped__ = True
  id = Column(Integer,primary_key=True)
  
class Address(BaseModel):
  __tablename__ = "address"
  city = Column(String)
  state = Column(String)
  zip_code = Column(Integer)
  user_id = Column(ForeignKey("users.id"))
  user = relationship("User",back_populates="address")
  
  def __repr__(self):
    return f"<Address:(id={self.id}),city={self.city},State={self.state},zip={self.zip_code},User={self.user}>"
  

class User(BaseModel):
  __tablename__ = "users"
  name = Column(String)
  age = Column(Integer)
  address = relationship(Address,back_populates="user")
  
  def __repr__(self):
    return f"<User:(id={self.id}),name={self.name},Address={self.address}>"
  
Base.metadata.create_all(bind=engine)  
  






