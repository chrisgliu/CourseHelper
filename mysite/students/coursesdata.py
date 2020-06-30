import requests
from django.contrib.sites.shortcuts import get_current_site


# --- get operations ---
# given the name of a major
# return related major data
def getCoursesAPI(request):
    current_site = get_current_site(request)
    api_domain = f"http://{current_site.domain}/courses/"
    return api_domain


def getMajorsList(request):
    majors = []
    api_request = getCoursesAPI(request) + 'majors/'
    result = requests.get(api_request)
    if result.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    for major in result.json():
        major_name = major.get("major")
        majors.append(major_name)
    return majors


def getMajorID(major_name):
    pass




def getMajorthing(major_name):
    pass