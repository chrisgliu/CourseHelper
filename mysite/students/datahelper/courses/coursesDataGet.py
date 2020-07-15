import requests
from django.conf import settings
import requests
from django.http import HttpResponse

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

