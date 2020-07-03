from .studentsDataGet import *
from ...models import *

# --- delete operations ---
# given user data and form data
# remove old related user data
def deleteStudent(user):
    old_student = getStudentID(user)
    old_student.delete()


def deleteMajor(user, major_name):
    old_major = getSpecificMajor(user, major_name)
    old_major.delete()


def deleteYear(user, year_name):
    old_year = getSpecificYear(user, year_name)
    old_year.delete()


def deleteSemester(user, year_name, semester_name):
    old_semester = getSpecificSemester(user, year_name, semester_name)
    old_semester.delete()


def deleteCourse(user, year_name, semester_name, course_name):
    old_course = getSpecificCourse(user, year_name, semester_name, course_name)
    old_course.delete()
