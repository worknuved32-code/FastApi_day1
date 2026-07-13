from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str
@app.post("/student")
def create_student(student:Student):
     return {
        "name": f"welcome {student.name}",
        "age": student.age,
        "course":student.course,
    }