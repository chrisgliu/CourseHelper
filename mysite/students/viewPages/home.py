from django.shortcuts import render
from ..dataforms.HelperForms import *
from ..dataforms.CoursesTemplate import *
# --- HOME PAGES ---
# home menu reflects if the user is logged in or not

all_forms = {
    'ListMajorForm':ListMajorForm,
    'ListCategoryForm':ListCategoryForm,
    'ListSubCategoryForm':ListSubCategoryForm,
    'ListRequirementForm':ListRequirementForm,
    'ListCourseForm':ListCourseForm,
    'ListPrereqForm':ListPrereqForm,
    'ListApForm':ListApForm,
    'MajorForm':MajorForm,
    'YearForm':YearForm,
    'SemesterForm':SemesterForm,
    'CourseForm':CourseForm
}

def mergeDict(x, y):
    z = x.copy()
    z.update(y)
    return z

# -- HOME MENU LINKS --
def getLoggedInNav(request):
    name = f'{request.user.first_name} {request.user.last_name}' 
    nav = {'signout':True, 'signin':False, 'signup':False, "name":name}
    return mergeDict(nav, all_forms)

def getLoggedOutNav():
    nav = {'signout':False, 'signin':True, 'signup':True}
    return mergeDict(nav, all_forms)
   
# --- HOME PAGES ---

def renderHome(request, template_path, more_context={}):
    if not request.user.is_authenticated:
        loggedOutContext = mergeDict(getLoggedOutNav(), more_context)
        return render(request=request, template_name=template_path, context=loggedOutContext)
    if request.user.is_authenticated:
        loggedInContext = mergeDict(getLoggedInNav(request), more_context)
        return render(request=request, template_name=template_path, context=loggedInContext)
