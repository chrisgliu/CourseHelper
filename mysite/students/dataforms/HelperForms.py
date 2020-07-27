from django import forms
from ..datahelper.students.studentsDataAdd import *
from ..datahelper.students.studentsDataDelete import *
from ..datahelper.students.studentsDataGet import *

# --- CREDIT PLANNER ---
class MajorForm(forms.Form):
    major = forms.CharField(label='major', required=True) 
    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        if add_or_delete == 'add':
            addMajor(request, major)
        if add_or_delete == 'delete':
            deleteMajor(request, major)


class YearForm(forms.Form):
    year = forms.CharField(label='year', required=True) 
    def process(self, request, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        if year == "before":
            year = request.user.username + "-before"
        if add_or_delete == 'add':
            if getSpecificYear(request, year) != -1:
                return
            addYear(request, year)
        if add_or_delete == 'delete':
            if year.find("before") != -1:
                return
            if getSpecificYear(request, year) == -1:
                return
            deleteYear(request, year)


class SemesterForm(forms.Form):
    year = forms.CharField(label='year', required=True) 
    semester = forms.CharField(label='semester', required=True) 
    def process(self, request, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        semester = self.cleaned_data.get('semester')
        if add_or_delete == 'add':
            if getSpecificSemester(request, year, semester) != -1:
                return
            addSemester(request, year, semester)
        if add_or_delete == 'delete':
            if getSpecificSemester(request, year, semester) == -1:
                return
            deleteSemester(request, year, semester)

class CourseForm(forms.Form):
    year = forms.CharField(label='years', required=True)
    semester = forms.CharField(label='semester', required=True)
    course = forms.CharField(label='course', required=True) 
    def process(self, request, add_or_delete='add'):
        year = self.cleaned_data.get('year')
        semester = self.cleaned_data.get('semester')
        course = self.cleaned_data.get('course')
        if add_or_delete == 'add':
            if getSpecificCourse(request, year, semester, course) != -1:
                return
            addCourse(request, year, semester, course)
        if add_or_delete == 'delete':
            if getSpecificCourse(request, year, semester, course) == -1:
                return
            deleteCourse(request, year, semester, course)

class APForm(forms.Form):
    test_name = forms.CharField(label='test_name', required=True)
    score = forms.CharField(label='score', required=True) 
    def process(self, request, add_or_delete='add'):
        test_name = self.cleaned_data.get('test_name')
        score = self.cleaned_data.get('score')
        if add_or_delete == 'add':
            addAP(request, test_name, score)
        if add_or_delete == 'delete':
            deleteAP(request, test_name, score) 


