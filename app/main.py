from fastapi import FastAPI
from schemas.StudentsSchema import StudentsSchema
from crud import read_student, create_student, update_student, delete_student


app = FastAPI(title="tutorial")


@app.get("/student")
def get_student():
    return read_student()


@app.post("/student")
async def post_student(student: StudentsSchema):
    newStudent = await create_student(student=student)
    print(newStudent)
    return "追加成功"


@app.put("/student/{id}")
def put_student(id: int, student: StudentsSchema):
    update_student(id=id, name=student.name, grade=student.grade)
    return "更新成功"


@app.delete("/student/{id}")
def del_student(id):
    delete_student(id=id)
    return "削除成功"
