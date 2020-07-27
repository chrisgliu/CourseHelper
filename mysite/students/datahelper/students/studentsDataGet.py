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
    year_before = request.user.username + "-before"
    if(user_years.filter(year=year_before).exists()==False):
        return [];
    year_object = user_years.filter(year=year_before).first() 
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
    year = Year.objects.filter(enrolled=key).filter(year=year_name)
    if year.exists():
        return year.first()
    else:
        return -1;


def getSpecificSemester(request, year_name, semester_name):
    year = getSpecificYear(request, year_name)
    semester = Semester.objects.filter(years=year).filter(semester=semester_name)
    if semester.exists():
        return semester.first()
    else:
        return -1;

def getSpecificCourse(request, year_name, semester_name, course_name):
    semester = getSpecificSemester(request, year_name, semester_name)
    course = Course.objects.filter(semesters=semester).filter(course=course_name)
    if course.exists():
        return course.first()
    else:
        return -1;

