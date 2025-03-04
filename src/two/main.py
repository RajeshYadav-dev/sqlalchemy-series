from database import engine,User
from sqlalchemy.orm import sessionmaker

  
Session = sessionmaker(bind=engine)

session = Session()

user1 = User(name="Rajesh",email="rajesh@gmail.com")
user2 = User(name="Rakesh",email="rakesh@gmail.com")
user3 = User(name="Ramesh",email="ramesh@gmail.com")

# create user
'''
session.add(user1) # add one user 
session.add_all([user2,user3]) #add multiple users
session.commit()
'''

# get all user

'''
users = session.query(User).all() # we will get a list  of users
for user in users:
  print(f"uid:{user.uid},name:{user.name},email:{user.email}")
'''

# get users by property
'''
users = session.query(User).filter_by(uid=1).all() # do'nt use one_or_none method
for user in users:
  print(f"uid:{user.uid},name:{user.name},email:{user.email}")
'''

# get user by property and get first one 
'''
user = session.query(User).filter_by(name="Rajesh").first() # do'nt use one_or_none method
print(f"uid:{user.uid},name:{user.name},email:{user.email}")
'''

# update user
'''
user = session.query(User).filter_by(uid=5).first()
user.name = "Raju"
session.commit()
'''

# delete user 
'''
user = session.query(User).filter_by(uid=5).first()
session.delete(user)
session.commit()
'''


  
