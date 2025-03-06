from database import session,Student,Course


math = Course(crs_name="Math",crs_duration=2)
java = Course(crs_name="Java",crs_duration=3)

raj = Student(std_name="Rajesh",std_age=23,course=[math,java])
ram = Student(std_name="Ram",std_age=28,course=[java])

session.add_all([math,java,raj,ram])
session.commit()