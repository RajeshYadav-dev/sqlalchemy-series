from database import session,User,Address


user1 = User(name="Rakesh",age=22)
user2 = User(name="Rajesh",age=32)

address1 = Address(city="munirka",state="Delhi",zip_code=110067)
address2 = Address(city="kishangarh",state="Delhi",zip_code=110088)
address3 = Address(city="vasant vihar",state="Delhi",zip_code=110066)

# associate address with user
user1.address.extend([address1,address2])
user2.address.append(address3)

# adding user and address to session and commiting to database
session.add(user1)
session.add(user2)
session.commit()

print(f"{user1}")
print(f"{user2}")
print(f"{address1}")
print(f"{address2}")
print(f"{address3}")