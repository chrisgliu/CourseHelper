from .coursesHelper import *
from .coursesDataGet import *
import requests

# --- delete operations ---
# given user data and form data
# remove old related user data

def deleteListStudent(request, first_name, last_name, username):
    instance_link = getStudentLink(request)
    requests.delete(instance_link)


def deleteListEnrollment(request):
    instance_link = getEnrollmentLink(request)
    requests.delete(instance_link)
    

def deleteListMajor(request, major_name):
    instance_links = getMajorLinks(request)
    instance_link = findInstanceLink(instance_links, 'major', major_name)
    requests.delete(instance_link)


def deleteListCategory(request, major_name, category_name):
    instance_links = getCategoryLinks(request)
    sub_links = filterLinks(request, instance_links, 'major', major_name)
    instance_link = findInstanceLink(sub_links, 'category', category_name)
    requests.delete(instance_link)


def deleteListSubCategory(request, category_name, subcategory_name):
    instance_links = getSubCategoryLinks(request)
    sub_links = filterLinks(request, instance_links, 'categories', category_name)
    instance_link = findInstanceLink(sub_links, 'subcategory', subcategory_name)
    requests.delete(instance_link)    

def deleteListRequirement(request, subcategory_name, requirement_name):
    instance_links = getRequirementLinks(request)
    sub_links = filterLinks(request, instance_links, 'subcategories', subcategory_name)
    instance_link = findInstanceLink(sub_links, 'requirement', requirement_name)
    requests.delete(instance_link)

def deleteListCourses(request, requirement_name, course_name):
    instance_links = getCourseLinks(request)
    sub_links = filterLinks(request, instance_links, 'requirements', requirement_name)
    instance_link = findInstanceLink(sub_links, 'course', course_name)
    requests.delete(instance_link)
 

def deleteListPrereq(request, course_name, prereq_name):
    instance_links = getPrereqLinks(request)
    sub_links = filterLinks(request, instance_links, 'courses', course_name)
    instance_link = findInstanceLink(sub_links, 'prereq', prereq_name)
    requests.delete(instance_link)


def deleteListAp(request, course_name, test_name, scoremin, scoremax):
    instance_links = getApLinks(request)
    sub_links = filterLinks(request, instance_links, 'courses', course_name)
    instance_link = findAPInstanceLink(sub_links, test_name, scoremin, scoremax)
    requests.delete(instance_link)
   