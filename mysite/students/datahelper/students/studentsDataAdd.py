from .studentsDataGet import *
from ...models import *

# --- add operations ---
# given user data and form data
# create new related user data
def addStudent(first_name, last_name, username):
    new_student = Student(firstname=first_name,
                          lastname=last_name,
                          username=username)
    new_student.save()


def addEnrollment(student):
    enroll = Enrolled(enrolled=True)
    enroll.students = student
    enroll.save()


def addMajor(user, major_name):
    key = getEnrollmentKey(user)
    new_major = Major(major=major_name)
    new_major.save()
    new_major.enrolled.add(key)
    new_major.save()


def addYear(user, year_name):
    key = getEnrollmentKey(user)
    new_year = Year(year=year_name)
    new_year.save()
    new_year.enrolled.add(key)
    new_year.save()


def addSemester(user, year_name, semester_name):
    year = getSpecificYear(user, year_name)
    new_semester = Semester(semester=semester_name)
    new_semester.save()
    new_semester.years.add(year)
    new_semester.save()


def addCourse(user, year_name, semester_name, course_name):
    semester = getSpecificSemester(user, year_name, semester_name)
    new_course = Course(course=course_name)
    new_course.save()
    new_course.semesters.add(semester)
    new_course.save()
