import requests
from django.contrib.sites.shortcuts import get_current_site


# --- get operations ---
# given the name of a major
# return related major data
def getCoursesAPI(request, data_set_num):
    data_sets = {
        0: 'majors',
        1: 'categories',
        2: 'subcategories',
        3: 'requirements',
        4: 'courses',
        5: 'prereqs',
        6: 'apcredits',
    }
    current_site = get_current_site(request)
    data_set = data_sets[data_set_num]
    api_domain = f"http://{current_site.domain}/courses/{data_set}/"
    return api_domain


def getMajorList(request):
    majors = []
    api_request = getCoursesAPI(request, 0)
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for major in result.json():
        major_name = major.get("major")
        majors.append(major_name)
    return majors


def checkValidMajor(request, major_name):
    api_request = getCoursesAPI(request, 0) + major_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    validity = True
    try: validity = result.json()['detail'] == "Not found."
    except KeyError: pass
    return validity


def getCategoryList(request, major_name):
    categories = []
    api_request = getCoursesAPI(request, 1)
    relation = api_request = getCoursesAPI(request, 0) + major_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for category in result.json():
        if category['major'] == relation:
            category_name = category['category']
            categories.append(category_name)
    return categories 

def getSubCategoryList(request, category_name):
    subcategories = []
    api_request = getCoursesAPI(request, 2)
    relation = api_request = getCoursesAPI(request, 1) + category_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for subcategory in result.json():
        if subcategory['category'] == relation:
            subcategory_name = subcategory['subcategory']
            subcategories.append(subcategory_name)
    return subcategories 

def getRequirementList(request, subcategory_name):
    requirenents = []
    api_request = getCoursesAPI(request, 3)
    relation = api_request = getCoursesAPI(request, 2) + subcategory_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for requirement in result.json():
        if requirement['subcategory'] == relation:
            requirement_name = requirement['requirement']
            requirenents.append(requirement_name)
    return requirenents


def getCourseList(request, requirement_name):
    courses = []
    api_request = getCoursesAPI(request, 4)
    relation = api_request = getCoursesAPI(request, 3) + requirement_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for course in result.json():
        if course['requirement'] == relation:
            course_name = course['course']
            courses.append(course_name)
    return courses 


def getPrereqList(request, course_name):
    prereqs = []
    api_request = getCoursesAPI(request, 5)
    relation = api_request = getCoursesAPI(request, 4) + course_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for prereq in result.json():
        if prereq['course'] == relation:
            prereq_name = prereq['prereq']
            prereqs.append(prereq_name)
    return prereqs 


def getAPList(request, course_name):
    apcredits = []
    api_request = getCoursesAPI(request, 6)
    relation = api_request = getCoursesAPI(request, 5) + course_name
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for apcredit in result.json():
        if apcredit['course'] == relation:
            ap_name = apcredit['test']
            apcredits.append(ap_name)
    return apcredits 




