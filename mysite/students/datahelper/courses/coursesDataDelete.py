import requests
from django.conf import settings
import requests
from django.http import HttpResponse

# --- delete operations ---
# given user data and form data
# remove old related user data
def deleteListStudent(request, first_name, last_name, username):
    data = { "firstname": first_name,"lastname": last_name,"username": username,}
    url = f'http://{settings.SITE_URL}/courses/deletestudent'
    action = requests.post(url, data=data)
    return action.status_code == 200

def deleteListEnrollment(request, username):
    data = { "username": username,}
    url = f'http://{settings.SITE_URL}/courses/deleteenrollkey'
    action = requests.post(url, data=data)
    return action.status_code == 200

def deleteListMajor(request, major_name):
    data = { "major": major_name,}
    url = f'http://{settings.SITE_URL}/courses/deletemajor'
    action = requests.post(url, data=data)
    return action.status_code == 200

def deleteListCategory(request, major_name, category_name):
    data = { "major": major_name,"category": category_name,}
    url = f'http://{settings.SITE_URL}/courses/deletecategory'
    action = requests.post(url, data=data)
    return action.status_code == 200

def deleteListSubCategory(request, major_name, category_name, subcategory_name, note):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name, "note": note,}
    url = f'http://{settings.SITE_URL}/courses/deletesubcategory'
    action = requests.post(url, data=data)
    return action.status_code == 200


def deleteListRequirement(request, major_name, category_name, subcategory_name, requirement_name, credit):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "credit": credit,}
    url = f'http://{settings.SITE_URL}/courses/deleterequirement'
    action = requests.post(url, data=data)
    return action.status_code == 200


def deleteListCourses(request, major_name, category_name, subcategory_name, requirement_name, course_name, credit):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "course": course_name, "credit": credit,}
    url = f'http://{settings.SITE_URL}/courses/deletecourse'
    action = requests.post(url, data=data)
    return action.status_code == 200


def deleteListPrereq(request, major_name, category_name, subcategory_name, requirement_name, course_name, prereq_name):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "course": course_name,"prereq": prereq_name,}
    url = f'http://{settings.SITE_URL}/courses/deleteprereq'
    action = requests.post(url, data=data)
    return action.status_code == 200


def deleteListAp(request, major_name, category_name, subcategory_name, requirement_name, course_name, test_name, scoremin, scoremax):
    data = { "major": major_name,"category": category_name,"subcategory": subcategory_name,"requirement": requirement_name, "course": course_name, "test": test_name, "scoremin": scoremin, "scoremax": scoremax,}
    url = f'http://{settings.SITE_URL}/courses/deleteap'
    action = requests.post(url, data=data)
    return action.status_code == 200

