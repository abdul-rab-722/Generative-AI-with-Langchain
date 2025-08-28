from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Abdul Rab'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'22', 'email':'abc@gmail.com'}

student = Student(**new_student)

# convert to dictionary
student_dict = dict(student)

print(student_dict['age'])

# convert to json
student_json = student.model_dump_json()