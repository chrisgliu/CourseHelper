import requests
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
import requests
from django.http import HttpResponse


# --- getting api link ---
data_sets = {
        'student': 'students','enrolled': 'enrolled','major': 'majors',
        'category': 'categories','subcategory': 'subcategories','requirement': 'requirements',
        'course': 'courses','prereq': 'prereqs','test': 'apcredits',
    }


def pluralVersion(data_model):
    data_set = data_sets.get(data_model)
    return data_set


def singularVersion(data_reference):
    for key, value in data_sets.items():
        if value == data_reference:
            return key

def getCoursesAPI(request, data_model):
    data_set = pluralVersion(data_model)
    api_domain = f'http://{settings.SITE_URL}/courses/{data_set}/'
    return api_domain


# --- getting the student ---
def getStudentInstances(request):
    instances = [] # entire student dir
    api_request = getCoursesAPI(request, 'student')
    result = requests.get(api_request)
    for i in result.json():
        instances.append(i)
    return instances

def getStudentInstancePK(request, username):
    instances = getStudentInstances(request)
    if request.user.is_authenticated: 
        username = request.user.username
    for i in instances:
        i_username = i.get("username")
        if i_username == username:
            return i.get('pk')
    return -1

# --- compile operations ----
def getSubDataLinks(request, data_model, parent_model, parent_link):
    sub_data_links = []
    api_request = getCoursesAPI(request, data_model)
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.') 
    for instance in result.json():
        parent_set = pluralVersion(parent_model)
        if parent_model == 'major' or parent_model=='enrolled':
            parent_set = parent_model
        if instance.get(parent_set) == parent_link or parent_link in instance.get(parent_set):
            i_pk = instance.get('pk')
            api_link = getCoursesAPI(request, data_model)
            i_link = f'{api_link}{i_pk}/' 
            sub_data_links.append(i_link)
    return sub_data_links


def compileSubDataLinks(request, data_model, parent_model, parent_links):
    all_sub_data_links = []
    for link in parent_links:
        sub_data_links = getSubDataLinks(request, data_model, parent_model, link)
        for sub_link in sub_data_links:
            all_sub_data_links.append(sub_link)
    return all_sub_data_links

# --- get operations ---
# given user data
# return links to related user data
def getStudentLink(request):
    pk = getStudentInstancePK(request, request.user.username)
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

# --- getting instance link ---
# used for deleting data
def findInstanceLink(instance_links, reference, name):
    i_link = None
    for link in instance_links:
        result = requests.get(link).json()
        if name == result.get(reference):
            i_link = link
    return i_link

def findAPInstanceLink(instance_links, test_name, scoremin, scoremax):
    i_link = None
    for link in instance_links:
        result = requests.get(link).json() 
        i_name = result.get('test')
        i_scoremin = result.get('scoremin')
        i_scoremax = result.get('scoremax')
        if i_name == test_name and i_scoremin == scoremin and i_scoremax == scoremax:
            i_link = link
    return i_link


# --- getting student instance data ---
# used for adding data
def getInstances(request, data_model):
    api_requests = []
    instances = []
    if data_model == 'enrolled': # search enitre dir for username
        api_request = getCoursesAPI(request, 'enrolled')
        result = requests.get(api_request)
        for i in result.json():
            instances.append(i)
        return instances
    elif data_model == 'major': # linked to student
        for api_request in getMajorLinks(request):
            api_requests.append(api_request)
    elif data_model == 'category': # linked to student
        for api_request in getCategoryLinks(request):
            api_requests.append(api_request)
    elif data_model == 'subcategory': # linked to student
        for api_request in getSubCategoryLinks(request):
            api_requests.append(api_request)
    elif data_model == 'requirement': # linked to student
        for api_request in getRequirementLinks(request):
            api_requests.append(api_request)
    elif data_model == 'course': # linked to student
        for api_request in getCourseLinks(request):
            api_requests.append(api_request)
    elif data_model == 'prereq': # linked to student
        for api_request in getPrereqLinks(request):
            api_requests.append(api_request)
    elif data_model == 'test': # linked to student
        for api_request in getApLinks(request):
            api_requests.append(api_request)
    for api_request in api_requests:
        result = requests.get(api_request)
        instances.append(result.json())
    return instances

def getAPInstancePK(request, test_name, scoremin, scoremax):
    instances = getInstances(request, 'test')
    for i in instances:
        i_name = i.get('test')
        i_min = i.get('scoremin')
        i_max = i.get('scoremax')
        if (i_name == test_name and i_min == scoremin and i_max==scoremax):
            return i.get('pk')
    return -1

def getInstancePK(request, data_model, name):
    instances = getInstances(request, data_model)
    for i in instances:
        i_name = i.get(data_model)
        if i_name == name:
            return i.get('pk')
    return -1

# --- get data list fuctions ---
# reads AJAX requests

def getMajorList(request):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/majorlist/{username}/'
    result = requests.get(url)
    return result.json().get('data')

def getCategoryList(request, major_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/categorylist/{username}/{major_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getSubCategoryList(request, major_name, category_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/subcategorylist/{username}/{major_name}/{category_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getRequirementList(request, major_name, category_name, subcategory_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/requirementlist/{username}/{major_name}/{category_name}/{subcategory_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getCourseList(request, major_name, category_name, subcategory_name, requirement_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/courselist/{username}/{major_name}/{category_name}/{subcategory_name}/{requirement_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getPrereqList(request, major_name, category_name, subcategory_name, requirement_name, course_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/prereqlist/{username}/{major_name}/{category_name}/{subcategory_name}/{requirement_name}/{course_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getAPList(request, major_name, category_name, subcategory_name, requirement_name, course_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/aplist/{username}/{major_name}/{category_name}/{subcategory_name}/{requirement_name}/{course_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getSubCategoryNote(request, major_name, category_name, subcategory_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/specificsubcategory/{username}/{major_name}/{category_name}/{subcategory_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getRequirementCredit(request, major_name, category_name, subcategory_name, requirement_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/specificrequirement/{username}/{major_name}/{category_name}/{subcategory_name}/{requirement_name}/'
    result = requests.get(url)
    return result.json().get('data')

def getCourseCredit(request, major_name, category_name, subcategory_name, requirement_name, course_name):
    username = request.user.username
    url = f'http://{settings.SITE_URL}/courses/specificcourse/{username}/{major_name}/{category_name}/{subcategory_name}/{requirement_name}/{course_name}/'
    result = requests.get(url)
    return result.json().get('data')

