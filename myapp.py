from typing import Optional

from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        'name': 'James',
        'age': 23,
        'class': 'year 12'
    }
}


@app.get('/')
def index():
    return {'a': 'Hello'}


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
