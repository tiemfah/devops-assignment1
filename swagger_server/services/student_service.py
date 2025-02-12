# student_service.py
from jsonschema import validate, ValidationError

from db.mongo_connection import students_collection

student_schema = {
    "type": "object",
    "required": ["first_name", "last_name"],
    "properties": {
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "student_id": {"type": "integer"},
    }
}


def get_next_student_id():
    last_student = students_collection.find_one(sort=[("student_id", -1)])
    if last_student:
        return last_student["student_id"] + 1
    return 1


def add(student=None):
    try:
        validate(instance=student.to_dict(), schema=student_schema)
    except ValidationError as e:
        return f"Invalid student data: {e.message}", 400

    query = {
        "first_name": student.first_name,
        "last_name": student.last_name
    }
    res = students_collection.find_one(query)
    if res:
        return 'already exists', 409

    student.student_id = get_next_student_id()
    students_collection.insert_one(student.to_dict())
    return student.student_id


def get_by_id(student_id=None, subject=None):
    student = students_collection.find_one({"student_id": student_id})
    if not student:
        return 'not found', 404
    # avoid serializing ObjectId, or I could write a custom JSONEncoder.
    del student["_id"]
    return student


def delete(student_id=None):
    result = students_collection.delete_one({"student_id": student_id})
    if result.deleted_count == 0:
        return 'not found', 404
    return student_id
