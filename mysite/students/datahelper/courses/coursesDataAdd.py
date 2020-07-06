from .coursesHelper import *
from .coursesDataGet import *
import requests

# --- add operations ---
# given user data and form data
# create new related user data for courses

def createData(request, data_model, data):
    api_link = getCoursesAPI(request, data_model)
    requests.post(api_link, data=data) 

def addRelation(request, data_model, relation, **kwargs):
    api_link = getCoursesAPI(request, data_model)
    instance_pk = 0
    if data_model == 'student':
        instance_pk = getStudentInstancePK(request)
    elif data_model == 'test':
        test = kwargs.get('test')
        scoremin = kwargs.get('scoremin')
        scoremax = kwargs.get('scoremax')
        instance_pk == getAPInstancePK(request, test, scoremin, scoremax)
    else:
        name = kwargs.get('name')
        instance_pk = getInstancePK(request, data_model, name)
    instance_link = f'{api_link}{instance_pk}/'
    requests.patch(instance_link, data=relation)


def addListStudent(request, first_name, last_name, username):
    data = { "firstname": first_name,"lastname": last_name,"username": username,}
    createData(request, 'student', data=data)


def addListEnrollment(request, username):
    student_relation = getStudentLink(request)
    data = { "enrolled": username,}
    relation = { "students": student_relation,}
    createData(request, 'enrolled', data=data)
    addRelation(request, 'enrolled', relation=relation, name=username)


def addListMajor(request, major_name):
    enrollment_relation = getEnrollmentLink(request)
    data = { "major": major_name,}
    relation = { "enrolled": enrollment_relation}
    createData(request, 'major', data=data)
    addRelation(request, 'major', relation=relation, name=major_name)
 

def addListCategory(request, major_name, category_name):
    major_relations = getMajorLinks(request)
    major_relation = filterLinks(request, major_relations, "major", major_name)
    data = { "category": category_name,}
    relation = { "major": major_relation}
    createData(request, 'category', data=data)
    addRelation(request, 'category', relation=relation, name=category_name)


def addListSubCategory(request, category_name, subcategory_name, note):
    category_relations = getCategoryLinks(request)
    category_relation = filterLinks(request, category_relations, "categories", category_name)
    data = { "subcategory": subcategory_name, "note": note,}
    relation = { "categories": category_relation}
    createData(request, 'subcategory', data=data)
    addRelation(request, 'subcategory', relation=relation, name=subcategory_name)

def addListRequirement(request, subcategory_name, requirement_name, credit):
    subcategory_relations = getSubCategoryLinks(request)
    subcategory_relation = filterLinks(request, subcategory_relations, "subcategories", subcategory_name)
    data = { "requirement": requirement_name, "credit": credit,}
    relation = { "subcategories": subcategory_relation}
    createData(request, 'requirement', data=data)
    addRelation(request, 'requirement', relation=relation, name=requirement_name)
   

def addListCourses(request, requirement_name, course_name, credit):
    requirement_relations = getRequirementLinks(request)
    requirement_relation = filterLinks(request, requirement_relations, "requirements", requirement_name)
    data = { "course": course_name, "credit": credit,}
    relation = { "requirements": requirement_relation}
    createData(request, 'course', data=data)
    addRelation(request, 'course', relation=relation, name=course_name)


def addListPrereq(request, course_name, prereq_name):
    course_relations = getCourseLinks(request)
    course_relation = filterLinks(request, course_relations, "courses", course_name)
    data = { "prereq": prereq_name,}
    relation = { "courses": course_relations}
    createData(request, 'prereq', data=data)
    addRelation(request, 'prereq', relation=relation, name=prereq_name)
    

def addListAp(request, course_name, test_name, scoremin, scoremax):
    course_relations = getCourseLinks(request)
    course_relation = filterLinks(request, course_relations, "courses", course_name)
    data = { "test": test_name, "scoremin": scoremin, "scoremax": scoremax,}
    relation = { "courses": course_relation}
    createData(request, 'test', data=data)
    addRelation(request, 'test', relation=relation, test=test_name, scoremin=scoremin, scoremax=scoremax)
   