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
    for instance in result.json():
        instances.append(instance)
    return instances

def getStudentInstancePK(request):
    instances = getInstances(request, 'student')
    if not request.user.is_authenticated:
            return -1
    if request.user.is_authenticated: 
        for instance in instances:
           instance_username = instance.get("username")
           username = request.user.username
           if instance_username == username:
                    return instance.get('pk')
    return -1

def getAPInstancePK(request, test_name, scoremin, scoremax):
    instances = getInstances(request, 'test')
    for instance in instances:
        _name = instance.get('test')
        _min = instance.get('scoremin')
        _max = instance.get('scoremax')
        if (_name == test_name and _min == scoremin and _max==scoremax):
            return instance.get('pk')
    return -1

def getInstancePK(request, data_model, name):
    instances = getInstances(request, data_model)
    for instance in instances:
        instance_name = instance.get(data_model)
        if instance_name == name:
            return instance.get('pk')
    return -1


def getInstanceNames(request, data_model, instance_links):
    names = []
    for instance in instance_links:
        result = requests.get(instance)
        name = result.json().get(data_model)
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
            instance_name = instance.get(data_model)
            instance_pk = getInstancePK(request, data_model, instance_name)
            api_link = getCoursesAPI(request, data_model)
            relation = f'{api_link}{instance_pk}/' 
            sub_data_links.append(relation)
    return sub_data_links


def compileSubDataLinks(request, data_model, parent_model, parent_links):
    all_sub_data_links = []
    for link in parent_links:
        sub_data_links = getSubDataLinks(request, data_model, parent_model, link)
        for sub_data_link in sub_data_links:
            all_sub_data_links.append(sub_data_link)
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
    instance_link = None
    for link in instance_links:
        result = requests.get(link).json()
        if name == result.get(reference):
            instance_link = link
    return instance_link