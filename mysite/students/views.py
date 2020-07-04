from .viewPages.authPages import *
from .viewPages.budgetPages import *
from .viewPages.creditPages import *
from .viewPages.homePages import *
from .viewPages.schedulePages import *
from django.views.decorators.csrf import csrf_protect
from .datahelper.courses.coursesDataGet import *

# Create your views here.

# --- TESTING --- 
def test(request):
    # return HttpResponse(getStudentLink(request))
    # return HttpResponse(str(getEnrollmentLink(request)))
    # return HttpResponse(str(getMajorLinks(request)))
    # return HttpResponse(str(getCategoryLinks(request)))
    # return HttpResponse(str(getSubCategoryLinks(request)))
    # return HttpResponse(str(getRequirementLinks(request)))
    # return HttpResponse(str(getCourseLinks(request)))
    # return HttpResponse(str(getPrereqLinks(request)))
    return HttpResponse(str(getApLinks(request)))


# --- ABOUT ---
def aboutPage(request):
    return renderHome(request, "students/about.html")

# --- AUTH ---
def signUpPage(request):
    return signUpPageHelper(request)


def signInPage(request):
    return signInPageHelper(request)


def signOut(request):
    return signOutHelper(request)


def activate(request, uidb64, token):
    return activateHelper(request, uidb64, token)

# --- AUTH FORMS ---
@csrf_protect
def signInForm(request):
    return signInFormHelper(request)

@csrf_protect
def signUpForm(request):
    return signUpFormHelper(request)

# --- HOME PAGES ---
def creditPage(request):
    return creditPageHelper(request)


def schedulePage(request):
    return schedulePageHelper(request)


def budgetPage(request):
    return budgetPageHelper(request)

# --- CREDIT FORMS ---
@csrf_protect
def creditAddMajor(request):
    return MajorFormAdd(request)

@csrf_protect
def creditDeleteMajor(request):
    return MajorFormDelete(request)

@csrf_protect
def creditAddYear(request):
    return YearFormAdd(request)

@csrf_protect
def creditDeleteYear(request):
    return YearFormDelete(request)

@csrf_protect
def creditAddSemester(request):
    return SemesterFormAdd(request)

@csrf_protect
def creditDeleteSemester(request):
    return SemesterFormDelete(request)

@csrf_protect
def creditAddCourse(request):
    return CourseFormAdd(request)

@csrf_protect
def creditDeleteCourse(request):
    return CourseFormDelete(request)

# # --- SCHEDULE FORMS ---
# @csrf_protect
# def scheduleForm(request):
#     pass

# # ---- BUDGET FORMS ---
# @csrf_protect
# def budgetForm(request):
#     pass


# --- COURSES REQUESTS ---
# return XML

def requestMajors(request):
    data = getMajorList(request)
    xml_response = getXMLString(data, 'majors', 'major') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestCategories(request, major_name):
    data = getCategoryList(request, major_name)
    xml_response = getXMLString(data, 'categories', 'category') 
    return HttpResponse(xml_response, content_type='text/xml')
   

def requestSubCategories(request, category_name):
    data = getSubCategoryList(request, category_name)
    xml_response = getXMLString(data, 'subcategories', 'subcategory') 
    return HttpResponse(xml_response, content_type='text/xml') 


def requestRequirements(request, subcategory_name):
    data = getRequirementList(request, subcategory_name)
    xml_response = getXMLString(data, 'requirements', 'requirement') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestCourses(request, requirement_name):
    data = getCourseList(request, requirement_name)
    xml_response = getXMLString(data, 'courses', 'course') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestPrereqs(request, course_name):
    data = getPrereqList(request, course_name)
    xml_response = getXMLString(data, 'prereqs', 'prereq') 
    return HttpResponse(xml_response, content_type='text/xml')


def requestAP(request, course_name):
    data = getAPList(request, course_name)
    xml_response = getXMLString(data, 'ap', 'test') 
    return HttpResponse(xml_response, content_type='text/xml')