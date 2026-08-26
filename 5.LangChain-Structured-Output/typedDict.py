from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person ={'name' :'nitish' , 'age' :35 }#even if 35 is string it won't raise a error


print(new_person)