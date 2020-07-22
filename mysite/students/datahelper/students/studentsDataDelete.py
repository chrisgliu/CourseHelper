from .studentsDataGet import *
from ...models import *

# --- delete operations ---
# given user data and form data
# remove old related user data
def deleteStudent(request):
    old_student = getStudentID(request)
    old_student.delete()


def deleteMajor(request, major_name):
    old_major = getSpecificMajor(request, major_name)
    old_major.delete()


def deleteYear(request, year_name):
    old_year = getSpecificYear(request, year_name)
    old_year.delete()


def deleteSemester(request, year_name, semester_name):
    old_semester = getSpecificSemester(request, year_name, semester_name)
    old_semester.delete()


def deleteCourse(request, year_name, semester_name, course_name):
    old_course = getSpecificCourse(request, year_name, semester_name, course_name)
    old_course.delete()

def deleteAP(request, test_name, score):
    tests = getAP(request)
    old_test = tests.filter(test=test_name).filter(score=score)
    old_test.delete()
