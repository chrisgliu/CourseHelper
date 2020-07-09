from ...models import *

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
        

def getSemesters(user, year):
    semesters = []
    if year in getYears(user):
        terms = Semester.objects.filter(years=year)
        for semester in terms:
            semesters.append(semester)
    return semesters


def getCourses(user, year, semester):
    courses = []
    if year in getYears(user) and semester in getSemesters(user, year):
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
