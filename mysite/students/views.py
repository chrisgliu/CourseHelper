from .viewPages.authPages import *
from .viewPages.creditPages import *
from .viewPages.homePages import *
from .viewPages.coursesPages import *
from django.views.decorators.csrf import csrf_protect
import requests
# Create your views here.

# --- TESTING --- 
def test(request):
    username = 'bsmith'
    data = { "enrolled": username,}

    api_link = getCoursesAPI(request, 'enrolled')
    result = requests.post(api_link, data)
    # createData(request, 'enrolled', data=data)
    # relation_pk = getStudentInstancePK(request, username)
    # data_pk = getInstancePK(request, 'enrolled', username)
    # addRelation('linkStudentAndEnrollment', relation_pk, data_pk)
    return HttpResponse(result)

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
def creditPageOne(request):
    return creditPageHelperOne(request)

def creditPageTwo(request):
    return creditPageHelperTwo(request)

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

# --- COURSES REQUESTS ---
# return XML
def requestMajors(request):
    return requestMajorsHelper(request)

def requestCategories(request, major_name):
    return requestCategoriesHelper(request, major_name)

def requestSubCategories(request, category_name):
    return requestSubCategoriesHelper(request, category_name)

def requestRequirements(request, subcategory_name):
    return requestRequirementsHelper(request, subcategory_name)

def requestCourses(request, requirement_name):
    return requestCoursesHelper(request, requirement_name)

def requestPrereqs(request, course_name):
    return requestPrereqsHelper(request, course_name)

def requestAP(request, course_name):
    return requestAPHelper(request, course_name)

# --- COURSES FORMS ---
@csrf_protect
def coursesAddMajor(request):
    return listMajorFormAdd(request)

@csrf_protect
def coursesDeleteMajor(request):
    return listMajorFormDelete(request)

@csrf_protect
def coursesAddCategory(request):
    return listCategoryFormAdd(request)

@csrf_protect
def coursesDeleteCategory(request):
    return listCategoryFormDelete(request)

@csrf_protect
def coursesAddSubCategory(request):
    return listSubCategoryFormAdd(request)

@csrf_protect
def coursesDeleteSubCategory(request):
    return listSubCategoryFormDelete(request)

@csrf_protect
def coursesAddRequirement(request):
    return listRequirementFormAdd(request)

@csrf_protect
def coursesDeleteRequirement(request):
    return listRequirementFormDelete(request)

@csrf_protect
def coursesAddCourse(request):
    return listCourseFormAdd(request)

@csrf_protect
def coursesDeleteCourse(request):
    return listCourseFormDelete(request)

@csrf_protect
def coursesAddPrereq(request):
    return listPrereqFormAdd(request)

@csrf_protect
def coursesDeletePrereq(request):
    return listPrereqFormDelete(request) 

@csrf_protect
def coursesAddAp(request):
    return listApFormAdd(request)

@csrf_protect
def coursesDeleteAp(request):
    return listApFormDelete(request)
