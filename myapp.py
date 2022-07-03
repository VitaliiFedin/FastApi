from typing import Optional

from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    cls_name: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    cls_name: Optional[str] = None


students = {
    1: {
        'name': 'James',
        'age': 23,
        'class_name': 'year 12'
    }
}


@app.get('/')
def index():
    return students


# path parameters
@app.get('/get-student/{student_id}')
def get_student(student_id: int = Path(None, description='Input the student ID', gt=0)):
    return students[student_id]


# query parameters
@app.get('/get-by-name')
def get_student(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'Data': 'Not found'}


@app.post('/create-student/{student_id}')
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"An error": "Student already exists"}
    students[student_id] = student
    return students[student_id]


@app.put('/update-student/{student_id}')
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student doesn't exists"}

    if student.name != None:
        students[student_id]['name'] = student.name

    if student.age != None:
        students[student_id]['age'] = student.age

    if student.cls_name != None:
        students[student_id]['class_name'] = student.cls_name

    return students[student_id]


@app.delete('/delete/{student_id}')
def delete_student(student_id: int):
    if student_id not in students:
        return {'Error': 'Student doesn\'t exists'}
    del students[student_id]
    return {"Message": 'Student was deleted'}
