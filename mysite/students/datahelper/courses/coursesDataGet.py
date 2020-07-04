from .coursesHelper import *
import requests
from lxml import etree

# --- get operations ---
# given user data
# return related major data


# --- get data links fuctions ---

def getStudentLink(request):
    pk = getInstancePK(request, 'student', request.user)
    api_link = getCoursesAPI(request, 'student')
    relation = f'{api_link}{pk}/'
    return relation
    
def getEnrollmentLink(request):
    student_link = getStudentLink(request)
    relations = getSubDataLinks(request, 'enrolled', 'student', student_link)
    return relations

def getMajorLinks(request):
    enrolled_link = getEnrollmentLink(request)
    relations = compileSubDataLinks(request, 'major', 'enrolled', enrolled_link)
    return relations

def getCategoryLinks(request):
    major_link = getMajorLinks(request) 
    relations = compileSubDataLinks(request, 'category', 'major', major_link)
    return relations

def getSubCategoryLinks(request):
    category_link = getCategoryLinks(request)
    relations = compileSubDataLinks(request, 'subcategory', 'category', category_link)
    return relations

def getRequirementLinks(request):
    subcategory_link = getSubCategoryLinks(request)
    relations = compileSubDataLinks(request, 'requirement', 'subcategory', subcategory_link)
    return relations

def getCourseLinks(request):
    req_link = getRequirementLinks(request)
    relations = compileSubDataLinks(request, 'course', 'requirement', req_link)
    return relations

def getPrereqLinks(request):
    course_link = getCourseLinks(request)
    relations = compileSubDataLinks(request, 'prereq', 'course', course_link)
    return relations

def getApLinks(request):
    course_link = getCourseLinks(request)
    relations = compileSubDataLinks(request, 'test', 'course', course_link)
    return relations

# %20 = space in url

# --- get data list fuctions ---
def getMajorList(request):
    links = getMajorLinks(request)
    data = getInstanceNames(request, 'major', links)
    return data


def getCategoryList(request, major_name):
    links = getCategoryLinks(request)
    filtered_links = filterLinks(request, links, 'major', major_name)
    data = getInstanceNames(request, 'category', filtered_links)
    return data

def getSubCategoryList(request, category_name):
    links = getSubCategoryLinks(request)
    filter_links = filterLinks(request, links, 'categories', category_name)
    data = getInstanceNames(request, 'subcategory', filter_links)
    return data

def getRequirementList(request, subcategory_name):
    links = getRequirementLinks(request)
    filter_links = filterLinks(request, links, 'subcategories', subcategory_name)
    data = getInstanceNames(request, 'requirement', filter_links)
    return data

def getCourseList(request, requirement_name):
    links = getCourseLinks(request)
    filter_links = filterLinks(request, links, 'requirements', requirement_name)
    data = getInstanceNames(request, 'course', filter_links)
    return data

def getPrereqList(request, course_name):
    links = getPrereqLinks(request)
    filter_links = filterLinks(request, links, 'courses', course_name)
    data = getInstanceNames(request, 'prereq', filter_links)
    return data

def getAPList(request, course_name):
    links = getApLinks(request)
    filter_links = filterLinks(request, links, 'courses', course_name)
    data = getInstanceNames(request, 'test', filter_links)
    return data

def getXMLString(data_list, data_set, data_model):
    root = etree.Element(data_set)
    length = etree.Element('length')
    length.text = str(len(data_list))
    root.append(length)
    for instance in data_list:
        model = etree.Element(data_model)
        model.text = instance       
        root.append(model)
    the_xml_string = etree.tostring(root, xml_declaration=True)
    return the_xml_string
