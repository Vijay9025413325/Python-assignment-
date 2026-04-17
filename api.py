from fastapi import FastAPI
from pydanctic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

#path parameter
@app.get("/user/{id}")
def get_user(id: int):
    return {"message": f"Hello, User {id}!"}

#query parameter
@app.get("/serach")
def search(name:str,age:int):
    return {"message": f"Hello, {name}! You are {age} years old."}

# post and model

class Student(BaseModel):
    id : int
    name : str
    age : int

students = []
@app.post("/student")
def create_student(student: Student):
    students.append(student)
    return {"message": f"Student {student.name} created successfully!"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: int):
    for student in students:
        if student.id == id:
            return student
    return {"message": "Student not found!"}


