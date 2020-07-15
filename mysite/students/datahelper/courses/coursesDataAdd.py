import requests
from django.conf import settings
import requests
from django.http import HttpResponse

# --- add operations ---
# given user data and form data
# create new related user data for courses
def addListStudent(request, first_name, last_name, username):
    data = { "firstname": first_name,"lastname": last_name,"username": username,}
    url = f'http://{settings.SITE_URL}/courses/createstudent'
    action = requests.post(url, data=data)
    return action.status_code == 200

def addListEnrollment(request, username):
    data = { "username": username,}
    url = f'http://{settings.SITE_URL}/courses/createenrollkey'
    action = requests.post(url, data=data)
    return action.status_code == 200

def addListMajor(request, major_name):
    data = { "major": major_name,}
    url = f'http://{settings.SITE_URL}/courses/createmajor'
    action = requests.post(url, data=data)
    return action.status_code == 200

def addListCategory(request, major_name, category_name):
    data = { "major": major_name,"category": category_name,}
    url = f'http://{settings.SITE_URL}/courses/createcategory'
    action = requests.post(url, data=data)
    return action.status_code == 200

def addListSubCategory(request, major_name, category_name, subcategory_name, note):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name, "note": note,}
    url = f'http://{settings.SITE_URL}/courses/createsubcategory'
    action = requests.post(url, data=data)
    return action.status_code == 200


def addListRequirement(request, major_name, category_name, subcategory_name, requirement_name, credit):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "credit": credit,}
    url = f'http://{settings.SITE_URL}/courses/createrequirement'
    action = requests.post(url, data=data)
    return action.status_code == 200


def addListCourses(request, major_name, category_name, subcategory_name, requirement_name, course_name, credit):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "course": course_name, "credit": credit,}
    url = f'http://{settings.SITE_URL}/courses/createcourse'
    action = requests.post(url, data=data)
    return action.status_code == 200


def addListPrereq(request, major_name, category_name, subcategory_name, requirement_name, course_name, prereq_name):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "course": course_name,"prereq": prereq_name,}
    url = f'http://{settings.SITE_URL}/courses/createprereq'
    action = requests.post(url, data=data)
    return action.status_code == 200


def addListAp(request, major_name, category_name, subcategory_name, requirement_name, course_name, test_name, scoremin, scoremax):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "course": course_name, "test": test_name, "scoremin": scoremin, "scoremax": scoremax,}
    url = f'http://{settings.SITE_URL}/courses/createap'
    action = requests.post(url, data=data)
    return action.status_code == 200

