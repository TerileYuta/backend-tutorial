from db import session
from schemas.StudentsSchema import StudentsSchema
from model import StudentsTable
from sqlalchemy import update, delete


def read_student():
    vars_student = (vars(student) for student in session.query(StudentsTable).all())
    return vars_student


def create_student(student: StudentsSchema):
    # student_data
    # [{
    # "id": 3,
    # "name": "Wasei",
    # "grade": 1
    # },
    # {
    # "id": 3,
    # "name": "Wasei",
    # "grade": 1
    # }]

    # **student.model_dump()
    # id = 3, name = "wasei", grade = 1
    new_student = StudentsTable(**student.model_dump())
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    return new_student


def update_student(id: int, name: str, grade: int):
    session.execute(
        update(StudentsTable)
        .where(StudentsTable.id == id)
        .values(name=name, grade=grade)
    )
    session.commit()


def delete_student(id):
    session.execute(delete(StudentsTable).where(StudentsTable.id == id))
    session.commit()
