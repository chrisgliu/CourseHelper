from .coursesHelper import *
from .coursesDataGet import *
import requests

# --- add operations ---
# given user data and form data
# create new related user data for courses

def performOperation(request, data_model, data):
    api_link = getCoursesAPI(request, data_model)
    requests.post(api_link, data=data)


def addListStudent(request, first_name, last_name, username):
    data = {
        "firstname": first_name,"lastname": last_name,"username": username,
    }
    performOperation(request, 'student', data)


def addListEnrollment(request):
    student_relation = getStudentLink(request)
    data = {
        "enrolled": True, "students": student_relation,
    }
    performOperation(request, 'enrolled', data)


def addListMajor(request, major_name):
    enrollment_relation = getEnrollmentLink(request)
    data = {
        "major": major_name, "enrolled": enrollment_relation,
    }
    performOperation(request, 'major', data)
 

def addListCategory(request, major_name, category_name):
    major_relations = getMajorLinks(request)
    major_relation = filterLinks(request, major_relations, "major", major_name)
    data = {
        "category": category_name, "major": major_relation, 
    }
    performOperation(request, 'category', data)


def addListSubCategory(request, category_name, subcategory_name, note):
    category_relations = getCategoryLinks(request)
    category_relation = filterLinks(request, category_relations, "categories", category_name)
    data = {
        "subcategory": subcategory_name, "note": note, "categories": category_relation, 
    }
    performOperation(request, 'subcategory', data)
    

def addListRequirement(request, subcategory_name, requirement_name, credit):
    subcategory_relations = getSubCategoryLinks(request)
    subcategory_relation = filterLinks(request, subcategory_relations, "subcategories", subcategory_name)
    data = {
        "requirement": requirement_name, "credit": credit, "subcategories": subcategory_relation, 
    }
    performOperation(request, 'requirement', data)


def addListCourses(request, requirement_name, course_name, credit):
    requirement_relations = getRequirementLinks(request)
    requirement_relation = filterLinks(request, requirement_relations, "requirements", requirement_name)
    data = {
        "course": course_name, "credit": credit, "requirements": requirement_relation, 
    }
    performOperation(request, 'course', data)


def addListPrereq(request, course_name, prereq_name):
    course_relations = getCourseLinks(request)
    course_relation = filterLinks(request, course_relations, "courses", course_name)
    data = {
        "prereq": prereq_name, "courses": course_relations, 
    }
    performOperation(request, 'prereq', data)
    

def addListAp(request, course_name, test_name, scoremin, scoremax):
    course_relations = getCourseLinks(request)
    course_relation = filterLinks(request, course_relations, "courses", course_name)
    data = {
        "test": test_name, "scoremin": scoremin, "scoremax": scoremax,"courses": course_relation, 
    }
    performOperation(request, 'test', data)
   