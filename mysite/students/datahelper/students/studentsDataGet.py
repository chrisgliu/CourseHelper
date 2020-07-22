from ...models import *

# --- get operations ---
# given user data (first name, last name, username)
# return related user data
def getStudentID(request):
    username = request.user.username
    return Student.objects.get(username=username)


def getEnrollmentKey(request):
    student_id = getStudentID(request)
    return Enrolled.objects.get(students=student_id)


def getMajors(request):
    key = getEnrollmentKey(request)
    return Major.objects.filter(enrolled=key)


def getYears(request):
    key = getEnrollmentKey(request)
    return Year.objects.filter(enrolled=key)

def getAP(request):
    user_years = getYears(request) 
    year_object = user_years.filter(year="before").first() 
    ap = []
    tests = AP.objects.filter(years__in=[year_object.pk])
    for test in tests:
        ap.append(test)
    return ap
        

def getSemesters(request, year):
    user_years = getYears(request)
    year_object = user_years.filter(year=year).first()
    semesters = []
    terms = Semester.objects.filter(years__in=[year_object.pk])
    for semester in terms:
        semesters.append(semester)
    return semesters


def getCourses(request, year, semester):
    user_years = getYears(request)
    year_object = user_years.filter(year=year).first()
    user_semesters = Semester.objects.filter(years__in=[year_object.pk])
    semester_object = user_semesters.filter(semester=semester).first()
    courses = []
    classes = Course.objects.filter(semesters__in=[semester_object.pk])
    for course in classes:
        courses.append(course)
    return courses


# --- specific ---
def getSpecificMajor(request, major_name):
    key = getEnrollmentKey(request)
    return Major.objects.get(enrolled=key, major=major_name)


def getSpecificYear(request, year_name):
    key = getEnrollmentKey(request)
    return Year.objects.get(enrolled=key, year=year_name)


def getSpecificSemester(request, year_name, semester_name):
    year = getSpecificYear(request, year_name)
    return Semester.objects.get(years=year, semester=semester_name)


def getSpecificCourse(request, year_name, semester_name, course_name):
    semester = getSpecificSemester(request, year_name, semester_name)
    return Course.objects.get(semesters=semester, course=course_name)

