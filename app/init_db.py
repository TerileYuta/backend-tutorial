from db import session
from schemas.StudentsSchema import StudentsSchema
from model import StudentsTable

sampleData = [
    StudentsSchema(name="Toya", grade=2),
    StudentsSchema(name="Kishida", grade=1),
]

for student in sampleData:
    new_student = StudentsTable(**student.model_dump())
    session.add(new_student)
    session.commit()