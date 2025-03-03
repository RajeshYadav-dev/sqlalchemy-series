import os 
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

'''
pip install sqlalchemy

  This is the general database_url format
  <dialect>+<driver>://<username>:<password>@<host>/<db_name>
  
  For MySQL
  mysql+pymysql://<username>:<password>@<host>/<db_name>
  Example: mysql+pymysql://root:password@localhost:3306/my_database
  
  For Postgres
  postgresql+psycopg2://<username>:<password>@<host>/<db_name>
  Example: postgresql+psycopg2://postgres:password@localhost:5432/my_database
  
  For SQLite
  sqlite:///./<db_name>.db
  Example: sqlite:///./my_database.db
  
  For MSSQL
  mssql+pyodbc://<username>:<password>@<host>/<db_name>?driver=ODBC+Driver+17+for+SQL+Server
  Example: mssql+pyodbc://sa:password@localhost:1433/my_database?driver=ODBC+Driver+17+for+SQL+Server
  
  For Oracle
  oracle+cx_oracle://<username>:<password>@<host>/<db_name>?service_name=<service_name>
  Example: oracle+cx_oracle://scott:tiger@localhost:1521/my_database?service_name=my_service
  
  
'''
  
os.makedirs("src\one\data", exist_ok=True)
# Set the database path
DATABASE_URL = "sqlite:///./src/one/data/database.db"

engine = create_engine(url=DATABASE_URL)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    
    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"
 


Base.metadata.create_all(bind=engine)

