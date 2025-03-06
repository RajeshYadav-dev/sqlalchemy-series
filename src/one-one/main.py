from database import session,User,Address


new_user = User(name="Rajesh",age=23) 
new_address = Address(city="Delhi",user=new_user)

session.add(new_address)
session.commit()
