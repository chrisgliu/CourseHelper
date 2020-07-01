from ..models import *

if __name__ == "__main__":
    print(Student.objects.all())
# --- get operations ---
# given user data (first name, last name, username)
# return related user data
def getStudentID(user):
    first_name = user.first_name
    last_name = user.last_name
    username = user.username
    return Student.objects.get(firstname=first_name,
                               lastname=last_name,
                               username=username)


def getEnrollmentKey(user):
    student_id = getStudentID(user)
    return Enrolled.objects.get(students=student_id)


def getMajors(user):
    key = getEnrollmentKey(user)
    return Major.objects.filter(enrolled=key)


def getYears(user):
    key = getEnrollmentKey(user)
    return Year.objects.filter(enrolled=key)


def getSemesters(user):
    semesters = []
    years = getYears(user)
    for year in years:
        terms = Semester.objects.filter(years=year)
        for semester in terms:
            semesters.append(semester)
    return semesters


def getCourses(user):
    courses = []
    semesters = getSemesters(user)
    for semester in semesters:
        classes = Course.objects.filter(semesters=semester)
        for course in classes:
            courses.append(course)
    return courses


# --- specific ---
def getSpecificMajor(user, major_name):
    key = getEnrollmentKey(user)
    return Major.objects.get(enrolled=key, major=major_name)


def getSpecificYear(user, year_name):
    key = getEnrollmentKey(user)
    return Year.objects.get(enrolled=key, year=year_name)


def getSpecificSemester(user, year_name, semester_name):
    year = getSpecificYear(user, year_name)
    return Semester.objects.get(years=year, semester=semester_name)


def getSpecificCourse(user, year_name, semester_name, course_name):
    semester = getSpecificSemester(user, year_name, semester_name)
    return Course.objects.get(semesters=semester, course=course_name)


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
