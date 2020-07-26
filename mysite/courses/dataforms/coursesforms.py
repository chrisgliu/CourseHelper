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

    def process(self, request, command='add'):
        firtsname = self.cleaned_data.get('firtsname')
        lastname = self.cleaned_data.get('lastname')
        username = self.cleaned_data.get('username')
        if command == 'add':
            createStudent(firtsname, lastname, username)
        if command == 'delete':
            deleteStudent(username)

class ListEnrollForm(forms.Form):
    username = forms.CharField(label='username', required=True)

    def process(self, request, command='add'):
        username = self.cleaned_data.get('username')
        if command == 'add':
            enroll_pk = createEnrollKey(username)
            student_pk = getStudent(username).pk
            linkStudentAndEnrollmentHelper(student_pk, enroll_pk)
        if command == 'delete':
            deleteEnrollKey(username)  

# commands create, add, delete

class ListMajorForm(forms.Form):
    major = forms.CharField(label='major', required=True) 
   
    def process(self, request, command='create'):
        major = self.cleaned_data.get('major')
        username = request.user.username
        if command == 'create':
            major_check = getMajor(username, major)
            major_pk = 0
            if major_check == -1:
                major_pk = createMajor(major)
            else:
                major_pk = major_check.pk
            enroll_pk = getEnrollKey(username).pk
            linkEnrollmentAndMajorHelper(enroll_pk, major_pk)
        if command == 'delete':
            deleteMajor(username, major) 


class ListCategoryForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True) 
    oldmajor = forms.CharField(label='oldmajor', required=False)  
    def process(self, request, command='create'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        oldmajor = self.cleaned_data.get('oldmajor') 
        username = request.user.username
        if command == 'create':
            category_check = getCategory(username, major, category)
            category_pk = 0
            if category_check == -1:
                category_pk = createCategory(category)
            else:
                category_pk = category_check.pk
            major_pk = getMajor(username, major).pk 
            linkMajorAndCategoryHelper(major_pk, category_pk)
        if command == 'delete':
            deleteCategory(username, major, category)
        if command == 'add':
            category_pk = getCategory(username, major, category).pk
            major_pk = getMajor(username, oldmajor).pk 
            linkMajorAndCategoryHelper(major_pk, category_pk)


class ListSubCategoryForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    note = forms.CharField(label='note', required=False)
    oldmajor = forms.CharField(label='oldmajor', required=False)  
    oldcategory = forms.CharField(label='oldcategory', required=False)
    def process(self, request, command='create'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        note = self.cleaned_data.get('note')
        oldmajor = self.cleaned_data.get('oldmajor')
        oldcategory = self.cleaned_data.get('oldcategory')  
        username = request.user.username
        if command == 'create':
            subcategory_check = getSubCategory(username, major, category, subcategory)
            subcategory_pk = 0
            if subcategory_check == -1:
                subcategory_pk = createSubcategory(subcategory, note)
            else:
                subcategory_pk = subcategory_check.pk
            category_pk = getCategory(username, major, category).pk
            linkCategoryAndSubcategoryHelper(category_pk, subcategory_pk)
        if command == 'delete':
            deleteSubcategory(username, major, category, subcategory)
        if command == 'add':
            subcategory_pk = getSubCategory(username, major, category, subcategory).pk
            category_pk = getCategory(username, oldmajor, oldcategory).pk
            linkCategoryAndSubcategoryHelper(category_pk, subcategory_pk)


class ListRequirementForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    credit = forms.IntegerField(label='credit', required=False)
    oldmajor = forms.CharField(label='oldmajor', required=False)  
    oldcategory = forms.CharField(label='oldcategory', required=False)
    oldsubcategory = forms.CharField(label='oldsubcategory', required=False)
    def process(self, request, command='create'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        credit = self.cleaned_data.get('credit')
        username = request.user.username
        oldmajor = self.cleaned_data.get('oldmajor')
        oldcategory = self.cleaned_data.get('oldcategory')  
        oldsubcategory = self.cleaned_data.get('oldsubcategory')  
        if command == 'create':
            requirement_check = getRequirement(username, major, category, subcategory, requirement)
            requirement_pk = 0
            if requirement_check == -1:
                requirement_pk = createRequirement(requirement, credit)
            else:
                requirement_pk = requirement_check.pk
            subcategory_pk = getSubCategory(username, major, category, subcategory).pk
            linkSubcategoryAndRequirementHelper(subcategory_pk, requirement_pk)
        if command == 'delete':
            deleteRequirement(username, major, category, subcategory, requirement) 
        if command == 'add': 
            requirement_pk = getRequirement(username, major, category, subcategory, requirement).pk
            subcategory_pk = getSubCategory(username, oldmajor, oldcategory, oldsubcategory).pk
            linkSubcategoryAndRequirementHelper(subcategory_pk, requirement_pk)


class ListCourseForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)
    credit = forms.IntegerField(label='credit', required=False)
    oldmajor = forms.CharField(label='major', required=False)  
    oldcategory = forms.CharField(label='category', required=False)
    oldsubcategory = forms.CharField(label='subcategory', required=False)
    oldrequirement = forms.CharField(label='requirement', required=False)

    def process(self, request, command='create'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        credit = self.cleaned_data.get('credit')
        username = request.user.username

        if command == 'create':
            course_check = getCourse(username, major, category, subcategory, requirement, course)
            course_pk = 0
            if course_check == -1:
                course_pk = createCourse(course, credit)
            else:
                course_pk = course_check.pk
            requirement_pk = getRequirement(username, major, category, subcategory, requirement)
            linkRequirementAndCourseHelper(requirement_pk, course_pk)
        if command == 'delete':
            deleteCourse(username, major, category, subcategory, requirement, course) 
        if command == 'add': 
            course_pk = getCourse(username, major, category, subcategory, requirement, course).pk
            requirement_pk = getRequirement(username, oldmajor, oldcategory, oldsubcategory, oldrequirement).pk
            linkRequirementAndCourseHelper(requirement_pk, course_pk)


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
    def process(self, request, command='add'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        pmajor = self.cleaned_data.get('pmajor')
        pcategory = self.cleaned_data.get('pcategory')
        psubcategory = self.cleaned_data.get('psubcategory')
        prequirement = self.cleaned_data.get('prequirement')
        pcourse = self.cleaned_data.get('pcourse')
        username = request.user.username
        if command == 'add':
            prereq_check = getPrereq(username, major, category, subcategory, requirement, course, pcourse)
            prereq_pk = 0
            if prereq_check == -1:
                prereq_pk = createPrereq(pcourse)
            else:
                prereq_pk = prereq_check.pk
            course_pk = getCourse(username, major, category, subcategory, requirement, course)
            linkCourseAndPrereqHelper(course_pk, prereq_pk)
        if command == 'delete':
            deletePrereq(username, major, category, subcategory, requirement, course, pcourse)


class ListApForm(forms.Form):
    major = forms.CharField(label='major', required=True)  
    category = forms.CharField(label='category', required=True)
    subcategory = forms.CharField(label='subcategory', required=True)
    requirement = forms.CharField(label='requirement', required=True)
    course = forms.CharField(label='course', required=True)
    skip = forms.CharField(label='skip', required=True)
    test = forms.CharField(label='test', required=True)
    scoremin = forms.IntegerField(label='scoremin', required=True)
    scoremax = forms.IntegerField(label='scoremax', required=True)
    oldmajor = forms.CharField(label='oldmajor', required=False)  
    oldcategory = forms.CharField(label='oldcategory', required=False)
    oldsubcategory = forms.CharField(label='oldsubcategory', required=False)
    oldrequirement = forms.CharField(label='oldrequirement', required=False)
    oldcourse = forms.CharField(label='oldcourse', required=False)

    def process(self, request, command='create'):
        major = self.cleaned_data.get('major')
        category = self.cleaned_data.get('category')
        subcategory = self.cleaned_data.get('subcategory')
        requirement = self.cleaned_data.get('requirement')
        course = self.cleaned_data.get('course')
        test = self.cleaned_data.get('test')
        scoremin = self.cleaned_data.get('scoremin')
        scoremax = self.cleaned_data.get('scoremax')
        username = request.user.username
        oldmajor = self.cleaned_data.get('oldmajor')
        oldcategory = self.cleaned_data.get('oldcategory')  
        oldsubcategory = self.cleaned_data.get('oldsubcategory')
        oldrequirement = self.cleaned_data.get('oldrequirement') 
        oldcourse = self.cleaned_data.get('oldcourse') 
        if command == 'create':
            ap_check = getTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax)
            ap_pk = 0
            if ap_check == -1:
                ap_pk = createAp(test, scoremin, scoremax)
            else:
                ap_pk = ap_check.pk
            course_pk = getCourse(username, oldmajor, oldcategory, oldsubcategory, oldrequirement, oldcourse).pk
            linkCourseAndApHelper(course_pk, ap_pk)
        if command == 'delete':
            deleteTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax)
        if command == 'add':
            ap_pk = getTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax).pk
            course_pk = getCourse(username, oldmajor, oldcategory, oldsubcategory, oldrequirement, oldcourse).pk
            linkCourseAndApHelper(course_pk, ap_pk)