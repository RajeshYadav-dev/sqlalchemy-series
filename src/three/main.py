from database import engine,User
from sqlalchemy.orm import sessionmaker
import random


Session = sessionmaker(bind=engine)

session = Session()

names = ["Rajesh","Rakesh","Ramesh","Naresh","Mukesh","Rupesh"]
ages = [12,32,45,23,32,12,23,45,32,44,33,22,]

'''
for x in range(20):
  user = User(name=random.choice(names),age=random.choice(ages))
  session.add(user)
session.commit()
'''
# query all student by age in ascendng order
# users = session.query(User).order_by(User.age).all()

# query all student by age in descending order
# users = session.query(User).order_by(User.age.desc()).all()

# Let use filter
# users = session.query(User).filter(User.age==12) # if present then return query of List else None

# users = session.query(User).filter_by(age=12).all() # if present then return query of List else None

# users = session.query(User).where(User.age<12) # retrun user age less than 12

# users = session.query(User).where((User.age>12) | (User.name=="Rajesh"))

users = session.query(User).where((User.age>12) & (User.name=="Rajesh"))

for user in users:
  print(f"ID:{user.uid}::NAME:{user.name}::AGE:{user.age}")
  
  
