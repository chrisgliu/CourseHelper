import requests
from django.contrib.sites.shortcuts import get_current_site


# --- get operations ---
# given the name of a major
# return related major data
def getCoursesAPI(request, data_model):
    data_sets = {
        'major': 'majors',
        'category': 'categories',
        'subcategory': 'subcategories',
        'requirement': 'requirements',
        'course': 'courses',
        'prereq': 'prereqs',
        'test': 'apcredits',
    }
    current_site = get_current_site(request)
    data_set = data_sets[data_model]
    api_domain = f'http://{current_site.domain}/courses/{data_set}/'
    return api_domain


def getInstancePK(request, data_model, name):
    api_request = getCoursesAPI(request, data_model) 
    result = requests.get(api_request)
    for instance in result.json():
        instance_name = instance[data_model]
        if instance_name == name:
            return instance.get('pk')
    return -1


def getMajorList(request):
    majors = []
    api_request = getCoursesAPI(request, 'major')
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for major in result.json():
        major_name = major['major']
        majors.append(major_name)
    return majors


def checkValidMajor(request, major_name):
    major_pk = getInstancePK(request, 'major', major_name)
    api_request = getCoursesAPI(request, 'major') + major_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    validity = True
    try: validity = result.json()['detail'] == 'Not found.'
    except KeyError: pass
    return validity


def getCategoryList(request, major_name):
    categories = []
    api_request = getCoursesAPI(request, 'category')
    major_pk = getInstancePK(request, 'major', major_name)
    relation = getCoursesAPI(request, 'major') + major_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for category in result.json():
        if category['major'] == relation:
            category_name = category['category']
            categories.append(category_name)
    return categories 


def getSubCategoryList(request, category_name):
    subcategories = []
    api_request = getCoursesAPI(request, 'subcategory')
    category_pk = getInstancePK(request, 'category', category_name)
    relation = api_request = getCoursesAPI(request, 'category') + category_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for subcategory in result.json():
        if subcategory['category'] == relation:
            subcategory_name = subcategory['subcategory']
            subcategories.append(subcategory_name)
    return subcategories 


def getRequirementList(request, subcategory_name):
    requirenents = []
    api_request = getCoursesAPI(request, 'requirement')
    subcategory_pk = getInstancePK(request, 'subcategory', subcategory_name) 
    relation = api_request = getCoursesAPI(request, 'subcategory') + subcategory_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for requirement in result.json():
        if requirement['subcategory'] == relation:
            requirement_name = requirement['requirement']
            requirenents.append(requirement_name)
    return requirenents


def getCourseList(request, requirement_name):
    courses = []
    api_request = getCoursesAPI(request, 'course')
    requirement_pk = getInstancePK(request, 'requirement', requirement_name) 
    relation = api_request = getCoursesAPI(request, 'requirement') + requirement_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for course in result.json():
        if course['requirement'] == relation:
            course_name = course['course']
            courses.append(course_name)
    return courses 


def getPrereqList(request, course_name):
    prereqs = []
    api_request = getCoursesAPI(request, 'prereq')
    course_pk = getInstancePK(request, 'course', course_name) 
    relation = api_request = getCoursesAPI(request, 'course') + course_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for prereq in result.json():
        if prereq['course'] == relation:
            prereq_name = prereq['prereq']
            prereqs.append(prereq_name)
    return prereqs 


def getAPList(request, course_name):
    apcredits = []
    api_request = getCoursesAPI(request, 'test')
    course_pk = getInstancePK(request, 'course', course_name) 
    relation = api_request = getCoursesAPI(request, 'course') + course_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    for apcredit in result.json():
        if apcredit['course'] == relation:
            ap_name = apcredit['test']
            apcredits.append(ap_name)
    return apcredits 




