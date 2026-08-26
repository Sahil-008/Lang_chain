from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    name : str = 'john' #default value if no value is provided
    age :Optional[int] = None #optional value if no value is provided

    #EmailStr is built-in data type in pydantic which checks if the value is a valid email or not
    #Field(gt ,lt) is used to check if the value is greater than or less than the specified value
new_student ={'name' : 'Sahil'}#error if the value is other data type then str
new2 = {}

student = Student(**new_student)
student1 = Student(**new2)
print(type(student))
print(student1.name)

student_dict = dict(student) #converts the object to dictionary
print(student_dict)

student_json = student.model_dump_json() #converts the object to json
print(student_json)