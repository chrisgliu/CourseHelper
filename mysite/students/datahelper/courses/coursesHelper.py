import requests
from django.contrib.sites.shortcuts import get_current_site

# --- helper functions ---

def pluralVersion(data_model):
    data_sets = {
        'student': 'students',
        'enrolled': 'enrolled',
        'major': 'majors',
        'category': 'categories',
        'subcategory': 'subcategories',
        'requirement': 'requirements',
        'course': 'courses',
        'prereq': 'prereqs',
        'test': 'apcredits',
    }
    data_set = data_sets[data_model] 
    return data_set

def getCoursesAPI(request, data_model):
    current_site = get_current_site(request)
    data_set = pluralVersion(data_model)
    api_domain = f'http://{current_site.domain}/courses/{data_set}/'
    return api_domain

def getInstances(request, data_model):
    instances = []
    api_request = getCoursesAPI(request, data_model) 
    result = requests.get(api_request)
    for instance in result.json():
        instances.append(instance)
    return instances

def getInstancePK(request, data_model, name):
    instances = getInstances(request, data_model)
    for instance in instances:
        if data_model=='student':
            instance_username = instance.get("username")
            user = name
            username = user.username
            if instance_username == username:
                return instance.get('pk')
        else:
            instance_name = instance.get(data_model)
            if instance_name == name:
                return instance.get('pk')
    return -1

def getInstanceNames(request, data_model, instance_links):
    names = []
    for instance in instance_links:
        result = requests.get(instance)
        name = result.get(data_model)
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

def filterLinks(links, parent_reference, parent_name):
    filtered_links = []
    for link in links:
        result = requests.get(link)
        if result.get(parent_reference) == parent_name:
            filtered_links.append(link)
    return filterLinks

def checkValidData(request, data_model, data_name):
    data_pk = getInstancePK(request, data_model, data_name)
    api_request = getCoursesAPI(request, data_model) + data_pk
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception('ERROR: API request unsuccessful.')
    validity = True
    try: validity = result.json()['detail'] == 'Not found.'
    except KeyError: pass
    return validity
