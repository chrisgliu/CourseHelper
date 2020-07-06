from .coursesHelper import *
from .coursesDataGet import *
import requests

# --- add operations ---
# given user data and form data
# create new related user data for courses

def createData(request, data_model, data):
    api_link = getCoursesAPI(request, data_model)
    requests.post(api_link, data=data) 


def addRelation(method_reference, relation_pk, data_pk):
    api_link = f'http://{settings.SITE_URL}/courses/{method_reference}/{relation_pk}/{data_pk}/'
    requests.get(api_link)


def addListStudent(request, first_name, last_name, username):
    data = { "firstname": first_name,"lastname": last_name,"username": username,}
    createData(request, 'student', data=data)


def addListEnrollment(request, username):
    data = { "enrolled": username,}
    createData(request, 'enrolled', data=data)
    relation_pk = getStudentInstancePK(request)
    data_pk = getInstancePK(request, 'enrolled', username)
    addRelation('linkStudentAndEnrollment', relation_pk, data_pk)


def addListMajor(request, major_name):
    data = { "major": major_name,}
    createData(request, 'major', data=data)
    relation_pk = getInstancePK(request, 'enrolled', request.user.username)
    data_pk = getInstancePK(request, 'major', major_name)
    addRelation('linkEnrollmentAndMajor', relation_pk, data_pk)
 

def addListCategory(request, major_name, category_name):
    data = { "category": category_name,}
    createData(request, 'category', data=data)
    relation_pk = getInstancePK(request, 'major', major_name)
    data_pk = getInstancePK(request, 'category', category_name)
    addRelation('linkMajorAndCategory', relation_pk, data_pk)

def addListSubCategory(request, category_name, subcategory_name, note):
    data = { "subcategory": subcategory_name, "note": note,}
    createData(request, 'subcategory', data=data)
    relation_pk = getInstancePK(request, 'category', category_name)
    data_pk = getInstancePK(request, 'subcategory', subcategory_name) 
    addRelation('linkCategoryAndSubcategory', relation_pk, data_pk)


def addListRequirement(request, subcategory_name, requirement_name, credit):
    data = { "requirement": requirement_name, "credit": credit,}
    createData(request, 'requirement', data=data)
    relation_pk = getInstancePK(request, 'subcategory', subcategory_name)
    data_pk = getInstancePK(request, 'requirement', requirement_name) 
    addRelation('linkSubcategoryAndRequirement', relation_pk, data_pk)


def addListCourses(request, requirement_name, course_name, credit):
    data = { "course": course_name, "credit": credit,}
    createData(request, 'course', data=data)
    relation_pk = getInstancePK(request, 'requirement', requirement_name)
    data_pk = getInstancePK(request, 'course', course_name)
    addRelation('linkRequirementAndCourse', relation_pk, data_pk)  


def addListPrereq(request, course_name, prereq_name):
    data = { "prereq": prereq_name,}
    createData(request, 'prereq', data=data)
    relation_pk = getInstancePK(request, 'course', course_name)
    data_pk = getInstancePK(request, 'prereq', prereq_name)
    addRelation('linkCourseAndPrereq', relation_pk, data_pk)


def addListAp(request, course_name, test_name, scoremin, scoremax):
    data = { "test": test_name, "scoremin": scoremin, "scoremax": scoremax,}
    createData(request, 'test', data=data)
    relation_pk = getInstancePK(request, 'course', course_name)
    data_pk = getAPInstancePK(request, test_name, scoremin, scoremax)
    addRelation('linkCourseAndAp', relation_pk, data_pk)