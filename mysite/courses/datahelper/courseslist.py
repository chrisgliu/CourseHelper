from lxml import etree
from django.http import JsonResponse
from ..models import *

# -- helper functions
def getStudent(username):
    student = Student.objects.get(username=username)
    return student

def getEnrollKey(username):
    enroll_key = Enrolled.objects.get(enrolled=username)
    return enroll_key

def getMajors(username):
    enroll_key = getEnrollKey(username)
    majors = Major.objects.filter(enrolled__in=[enroll_key.pk])
    return majors

def getMajor(username, major_name):
    majors = getMajors(username)
    the_major = majors.filter(major=major_name)
    if the_major.exists():
        return the_major.first()
    else:
        return -1

def getCategories(major):
    categories = Category.objects.filter(major__in=[major.pk])
    return categories

def getCategory(username, major_name, category_name):
    the_major = getMajor(username, major_name)
    categories = getCategories(the_major)
    the_category = categories.filter(category=category_name)
    if the_category.exists():
        return the_category.first()
    else:
        return -1 

def getSubCategories(category):
    subcategories = SubCategory.objects.filter(categories__in=[category.pk])
    return subcategories

def getSubCategory(username, major_name, category_name, subcategory_name):
    the_category = getCategory(username, major_name, category_name)
    subcategories = getSubCategories(the_category)
    the_subcategory = subcategories.filter(subcategory=subcategory_name)
    if the_subcategory.exists():
        return the_subcategory.first()
    else:
        return -1;

def getRequirements(subcategory):
    requirements = Requirement.objects.filter(subcategories__in=[subcategory.pk])
    return requirements

def getRequirement(username, major_name, category_name, subcategory_name, requirement_name):
    the_subcategory = getSubCategory(username, major_name, category_name, subcategory_name)
    requirements = getRequirements(the_subcategory)
    the_requirement = requirements.filter(requirement=requirement_name)
    if the_requirement.exists():
        return the_requirement.first()
    else:
        return -1;



def getCourses(requirement):
    courses = Course.objects.filter(requirements__in=[requirement.pk])
    return courses

def getCourse(username, major_name, category_name, subcategory_name, requirement_name, course_name):
    the_requirement = getRequirement(username, major_name, category_name, subcategory_name, requirement_name)
    courses = getCourses(the_requirement)
    the_course = courses.filter(course=course_name)
    if the_course.exists():
        return the_course.first()
    else:
        return -1;

def getPrereqs(course):
    prereqs = Prereq.objects.filter(courses__in=[course.pk])
    return prereqs

def getPrereq(username, major_name, category_name, subcategory_name, requirement_name, course_name, prereq_name):
    the_course = getCourse(username, major_name, category_name, subcategory_name, requirement_name, course_name)
    prereqs = getPrereqs(the_course)
    the_prereq = prereqs.filter(prereq=prereq_name)
    if the_prereq.exists():
        return the_prereq.first()
    else:
        return -1; 

def getAp(course):
    ap = ApCredit.objects.filter(courses__in=[course.pk])
    return ap

def getTest(username, major_name, category_name, subcategory_name, requirement_name, course_name, test, scoremin, scoremax):
    the_course = getCourse(username, major_name, category_name, subcategory_name, requirement_name, course_name)
    ap = getAp(the_course)
    the_test = ap.filter(test=test).filter(scoremin=scoremin).filter(scoremax=scoremax)
    if the_test.exists():
        return the_test.first()
    else:
        return -1; 

# --- data list helper functions --
def requestMajorListHelper(request, username):
    majors = getMajors(username)
    major_list = []
    for major_object in majors:
        major_list.append(major_object.major)
    return JsonResponse({'data':major_list})

def requestCategoriesListHelper(request, username, major_name):
    the_major = getMajor(username, major_name)
    categories = getCategories(the_major)
    category_list = []
    for category_object in categories:
        category_list.append(category_object.category)
    return JsonResponse({'data':category_list})

def requestSubcategoriesListHelper(request, username, major_name, category_name):
    the_category = getCategory(username, major_name, category_name)
    subcategories = getSubCategories(the_category)
    subcategory_list = []
    for subcategory_object in subcategories:
        subcategory_list.append(subcategory_object.subcategory)
    return JsonResponse({'data':subcategory_list})

def requestRequirementsListHelper(request, username, major_name, category_name, subcategory_name):
    the_subcategory = getSubCategory(username, major_name, category_name, subcategory_name)
    requirements = getRequirements(the_subcategory)
    requirement_list = []
    for requirement_object in requirements:
        requirement_list.append(requirement_object.requirement)
    return JsonResponse({'data':requirement_list})

def requestCoursesListHelper(request, username, major_name, category_name, subcategory_name, requirement_name):
    the_requirement = getRequirement(username, major_name, category_name, subcategory_name, requirement_name) 
    courses = getCourses(the_requirement)
    course_list = []
    for course_object in courses:
        course_list.append(course_object.course)
    return JsonResponse({'data':course_list})

def requestPrereqListHelper(request, username, major_name, category_name, subcategory_name, requirement_name, course_name):
    the_course = getCourse(username, major_name, category_name, subcategory_name, requirement_name, course_name)
    prereqs = getPrereqs(the_course)
    prereq_list = []
    for prereq_object in prereqs:
        prereq_list.append(prereq_object.prereq)
    return JsonResponse({'data':prereq_list})

def requestApListHelper(request, username, major_name, category_name, subcategory_name, requirement_name, course_name):
    the_course = getCourse(username, major_name, category_name, subcategory_name, requirement_name, course_name)
    ap = getAp(the_course)
    ap_list = []
    for test_object in ap:
        test_name = test_object.test
        test_min = test_object.scoremin
        test_max = test_object.scoremax 
        test_id = f"{test_name}/{test_min}/{test_max}"
        ap_list.append(test_id)
    return JsonResponse({'data':ap_list})

# --- request specific info ---
def requestSubcategoryNoteHelper(request, username, major_name, category_name, subcategory_name):
    the_subcategory = getSubCategory(username, major_name, category_name, subcategory_name)
    note = the_subcategory.note
    return JsonResponse({'data':note})

def requestRequirementCreditHelper(request, username, major_name, category_name, subcategory_name, requirement_name):
    the_requirement = getRequirement(username, major_name, category_name, subcategory_name, requirement_name) 
    credit = str(the_requirement.credit)
    return JsonResponse({'data':credit})

def requestCoursesCreditHelper(request, username, major_name, category_name, subcategory_name, requirement_name, course_name):
    the_course = getCourse(username, major_name, category_name, subcategory_name, requirement_name, course_name)
    credit = str(the_course.credit)
    return JsonResponse({'data':credit})


