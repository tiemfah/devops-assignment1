import connexion

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.services import student_service


def add_student(body=None):  # noqa: E501
    """Add a new student

    Adds an item to the system # noqa: E501

    :param body: Student item to add
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())  # noqa: E501
        return student_service.add(body)
    return 500, 'Error'


def delete_student(student_id):  # noqa: E501
    """deletes a student

    delete a single student  # noqa: E501

    :param student_id: student_id, an integer
    :type student_id: int

    :rtype: object
    """
    return student_service.delete(student_id)


def get_student_by_id(student_id):  # noqa: E501
    """gets student

    Returns a single student # noqa: E501

    :param student_id: student_id, an integer
    :type student_id: int

    :rtype: Student
    """
    return student_service.get_by_id(student_id)
