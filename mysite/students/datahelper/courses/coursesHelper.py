import requests
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

# --- helper functions ---
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


def getInstances(request, data_model):
    instances = []
    api_request = getCoursesAPI(request, data_model) 
    result = requests.get(api_request)
    for i in result.json():
        instances.append(i)
    return instances

def getStudentInstancePK(request):
    instances = getInstances(request, 'student')
    if not request.user.is_authenticated:
            return -1
    if request.user.is_authenticated: 
        for i in instances:
           i_username = i.get("username")
           username = request.user.username
           if i_username == username:
                return i.get('pk')
    return -1

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


def getInstanceNames(request, data_model, instance_links):
    names = []
    for i in instance_links:
        result = requests.get(i).json()
        name = result.get(data_model)
        if data_model == 'test':
            scoremin = result.get('scoremin')
            scoremax = result.get('scoremax')
            name = f'{name}:{scoremin}-{scoremax}'
        names.append(name)
    return names


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
        if instance[parent_set] == parent_link or parent_link in instance[parent_set]:
            i_name = instance.get(data_model)
            i_pk = getInstancePK(request, data_model, i_name)
            if data_model == 'test':
                i_scoremin = instance.get('scoremin')
                i_scoremax = instance.get('scoremax')
                i_pk = getAPInstancePK(request, i_name, i_scoremin, i_scoremax)
            api_link = getCoursesAPI(request, data_model)
            relation = f'{api_link}{i_pk}/' 
            sub_data_links.append(relation)
    return sub_data_links


def compileSubDataLinks(request, data_model, parent_model, parent_links):
    all_sub_data_links = []
    for link in parent_links:
        sub_data_links = getSubDataLinks(request, data_model, parent_model, link)
        for sub_link in sub_data_links:
            all_sub_data_links.append(sub_link)
    return all_sub_data_links


def filterLinks(request, links, parent_reference, parent_name):
    filtered_links = []
    parent_model = 'major'
    if parent_reference != 'major':
        parent_model = singularVersion(parent_reference)
    parent_pk = getInstancePK(request, parent_model, parent_name)
    api_link = getCoursesAPI(request, parent_model)
    parent_relation = f'{api_link}{parent_pk}/' 
    for link in links:
        result = requests.get(link).json()
        if parent_relation in result.get(parent_reference):
            filtered_links.append(link)
    return filtered_links


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