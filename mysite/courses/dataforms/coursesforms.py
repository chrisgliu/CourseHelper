from django import forms
from ..datahelper.coursesadd import *
from ..datahelper.coursesrelation import *
from ..datahelper.courseslist import *
from ..datahelper.coursesdelete import *
# --- COURSES DATA ---
class ListStudentForm(forms.Form):
    firstname = forms.CharField(label='firstname', required=True)
    lastname = forms.CharField(label='lastname', required=True)
    username = forms.CharField(label='username', required=True)

    def process(self, request, add_or_delete='add'):
        firtsname = self.cleaned_data.get('firtsname')
        lastname = self.cleaned_data.get('lastname')
        username = self.cleaned_data.get('username')
        if add_or_delete == 'add':
            createStudent(firtsname, lastname, username)
        if add_or_delete == 'delete':
            deleteStudent(username)

class ListEnrollForm(forms.Form):
    username = forms.CharField(label='username', required=True)

    def process(self, request, add_or_delete='add'):
        username = self.cleaned_data.get('username')
        if add_or_delete == 'add':
            enroll_pk = createEnrollKey(username)
            student_pk = getStudent(username).pk
            linkStudentAndEnrollmentHelper(student_pk, enroll_pk)
        if add_or_delete == 'delete':
            deleteEnrollKey(username)  

class ListMajorForm(forms.Form):
    major = forms.CharField(label='major', required=True) 
   
    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        username = request.user.username

        if add_or_delete == 'add':
            major_check = getMajor(username, major)
            major_pk = 0
            if major_check == -1:
                major_pk = createMajor(major)
            else:
                major_pk = major_check.pk
            enroll_pk = getEnrollKey(username).pk
            linkEnrollmentAndMajorHelper(enroll_pk, major_pk)
        if add_or_delete == 'delete':
            deleteMajor(username, major) 


class ListCategoryForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True) 
    
    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        username = request.user.username

        if add_or_delete == 'add':
            category_check = getCategory(username, major, category)
            category_pk = 0
            if category_check == -1:
                category_pk = createCategory(category)
            else:
                category_pk = category_check.pk
            major_pk = getMajor(username, major).pk 
            linkMajorAndCategoryHelper(major_pk, category_pk)
        if add_or_delete == 'delete':
            deleteCategory(username, major, category)


class ListSubCategoryForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    note = forms.CharField(label='note', required=False)

    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        note = self.cleaned_data.get('note')
        username = request.user.username

        if add_or_delete == 'add':
            subcategory_check = getSubCategory(username, major, category, subcategory)
            subcategory_pk = 0
            if subcategory_check == -1:
                subcategory_pk = createSubcategory(subcategory, note)
            else:
                subcategory_pk = subcategory_check.pk
            category_pk = getCategory(username, major, category).pk
            linkCategoryAndSubcategoryHelper(category_pk, subcategory_pk)
        if add_or_delete == 'delete':
            deleteSubcategory(username, major, category, subcategory)


class ListRequirementForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    credit = forms.IntegerField(label='credit', required=False)

    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        credit = self.cleaned_data.get('credit')
        username = request.user.username

        if add_or_delete == 'add':
            requirement_check = getRequirement(username, major, category, subcategory, requirement)
            requirement_pk = 0
            if requirement_check == -1:
                requirement_pk = createRequirement(requirement, credit)
            else:
                requirement_pk = requirement_check.pk
            subcategory_pk = getSubCategory(username, major, category, subcategory).pk
            linkSubcategoryAndRequirementHelper(subcategory_pk, requirement_pk)
        if add_or_delete == 'delete':
            deleteRequirement(username, major, category, subcategory, requirement) 

class ListCourseForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)
    credit = forms.IntegerField(label='credit', required=False)

    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        credit = self.cleaned_data.get('credit')
        username = request.user.username

        if add_or_delete == 'add':
            course_check = getCourse(username, major, category, subcategory, requirement, course)
            course_pk = 0
            if course_check == -1:
                course_pk = createCourse(course, credit)
            else:
                course_pk = course_check.pk
            requirement_pk = getRequirement(username, major, category, subcategory, requirement)
            linkRequirementAndCourseHelper(requirement_pk, course_pk)
        if add_or_delete == 'delete':
            deleteCourse(username, major, category, subcategory, requirement, course) 


class ListPrereqForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)
    pmajor = forms.CharField(label='pmajor', required=True)  
    pcategory = forms.CharField(label='pcategory', required=True)
    psubcategory = forms.CharField(label='psubcategory', required=True)
    prequirement = forms.CharField(label='prequirement', required=True)
    pcourse = forms.CharField(label='pcourse', required=True)

    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        prereq = self.cleaned_data.get('pcourse')
        username = request.user.username

        if add_or_delete == 'add':
            prereq_check = getPrereq(username, major, category, subcategory, requirement, course, prereq)
            prereq_pk = 0
            if prereq_check == -1:
                prereq_pk = createPrereq(prereq)
            else:
                prereq_pk = prereq_check.pk
            course_pk = getCourse(username, major, category, subcategory, requirement, course)
            linkCourseAndPrereqHelper(course_pk, prereq_pk)
        if add_or_delete == 'delete':
            deletePrereq(username, major, category, subcategory, requirement, course, prereq)

class ListApForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)
    test = forms.CharField(label='test', required=True)
    scoremin = forms.IntegerField(label='scoremin', required=True)
    scoremax = forms.IntegerField(label='scoremax', required=True)

    def process(self, request, add_or_delete='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        test = self.cleaned_data.get('test')
        scoremin = self.cleaned_data.get('scoremin')
        scoremax = self.cleaned_data.get('scoremax')
        username = request.user.username

        if add_or_delete == 'add':
            ap_check = getTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax)
            ap_pk = 0
            if ap_check == -1:
                ap_pk = createAp(test, scoremin, scoremax)
            else:
                ap_pk = ap_check.pk
            course_pk = getCourse(username, major, category, subcategory, requirement, course)
            linkCourseAndApHelper(course_pk, ap_pk)
        if add_or_delete == 'delete':
            deleteTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax)

