from django.urls import reverse
from .dataforms.coursesforms import *
from django.http import HttpResponse

# --- COURSES FORMS ---
# post redirect get 
def processForm(request, model_form, command):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = model_form(request.POST)
            if form.is_valid():
                form.process(request, command)
                return HttpResponse("hello")
            else:
                return HttpResponse("invalid form"+str(form))
        else: return HttpResponse("invalid user")
    return HttpResponse("other")

def CourseStudentFormAdd(request):
    return processForm(request, ListStudentForm, 'add')

def CourseStudentFormDelete(request):
    return processForm(request, ListStudentForm, 'delete')

def CourseEnrollFormAdd(request):
    return processForm(request, ListEnrollForm, 'add')

def CourseEnrollFormDelete(request):
    return processForm(request, ListEnrollForm, 'delete')

def CourseMajorFormAdd(request):
    return processForm(request, ListMajorForm, 'create')

def CourseMajorFormDelete(request):
    return processForm(request, ListMajorForm, 'delete')

def CourseCategoryFormCreate(request):
    return processForm(request, ListCategoryForm, 'create')

def CourseCategoryFormAdd(request):
    return processForm(request, ListCategoryForm, 'add')

def CourseCategoryFormDelete(request):
    return processForm(request, ListCategoryForm, 'delete')

def CourseSubCategoryFormCreate(request):
    return processForm(request, ListSubCategoryForm, 'create')

def CourseSubCategoryFormAdd(request):
    return processForm(request, ListSubCategoryForm, 'add')

def CourseSubCategoryFormDelete(request):
    return processForm(request, ListSubCategoryForm, 'delete')

def CourseRequirementFormCreate(request):
    return processForm(request, ListRequirementForm, 'create')

def CourseRequirementFormAdd(request):
    return processForm(request, ListRequirementForm, 'add')

def CourseRequirementFormDelete(request):
    return processForm(request, ListRequirementForm, 'delete')

def CourseCourseFormCreate(request):
    return processForm(request, ListCourseForm, 'create')

def CourseCourseFormAdd(request):
    return processForm(request, ListCourseForm, 'add')

def CourseCourseFormDelete(request):
    return processForm(request, ListCourseForm, 'delete')

def CoursePrereqFormAdd(request):
    return processForm(request, ListPrereqForm, 'add')

def CoursePrereqFormDelete(request):
    return processForm(request, ListPrereqForm, 'delete')

def CourseApFormCreate(request):
    return processForm(request, ListApForm, 'create')

def CourseApFormAdd(request):
    return processForm(request, ListApForm, 'add')

def CourseApFormDelete(request):
    return processForm(request, ListApForm, 'delete')

