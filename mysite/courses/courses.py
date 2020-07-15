from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .dataforms.coursesforms import *

# --- COURSES FORMS ---
def processForm(request, model_form, command):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request, command)
                return HttpResponse('complete')
    return HttpResponse('an error occured')

def listStudentFormAdd(request):
    return processForm(request, ListStudentForm, 'add')

def listStudentFormDelete(request):
    return processForm(request, ListStudentForm, 'delete')

def listEnrollFormAdd(request):
    return processForm(request, ListEnrollForm, 'add')

def listEnrollFormDelete(request):
    return processForm(request, ListEnrollForm, 'delete')

def listMajorFormAdd(request):
    return processForm(request, ListMajorForm, 'add')

def listMajorFormDelete(request):
    return processForm(request, ListMajorForm, 'delete')

def listCategoryFormAdd(request):
    return processForm(request, ListCategoryForm, 'add')

def listCategoryFormDelete(request):
    return processForm(request, ListCategoryForm, 'delete')

def listSubCategoryFormAdd(request):
    return processForm(request, ListSubCategoryForm, 'add')

def listSubCategoryFormDelete(request):
    return processForm(request, ListSubCategoryForm, 'delete')

def listRequirementFormAdd(request):
    return processForm(request, ListRequirementForm, 'add')

def listRequirementFormDelete(request):
    return processForm(request, ListRequirementForm, 'delete')

def listCourseFormAdd(request):
    return processForm(request, ListCourseForm, 'add')

def listCourseFormDelete(request):
    return processForm(request, ListCourseForm, 'delete')

def listPrereqFormAdd(request):
    return processForm(request, ListPrereqForm, 'add')

def listPrereqFormDelete(request):
    return processForm(request, ListPrereqForm, 'delete')

def listApFormAdd(request):
    return processForm(request, ListApForm, 'add')

def listApFormDelete(request):
    return processForm(request, ListApForm, 'delete')

