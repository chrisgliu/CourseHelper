from ..models import *

# --- manipulate relationships ---
def linkStudentAndEnrollmentHelper(student_pk, enrollment_pk):
    student = Student.objects.get(pk=student_pk)
    enrolled = Enrolled.objects.get(pk=enrollment_pk)
    enrolled.students = student
    enrolled.save()

def linkEnrollmentAndMajorHelper(enrollment_pk, major_pk):
    enrolled = Enrolled.objects.get(pk=enrollment_pk)
    major = Major.objects.get(pk=major_pk)
    major.enrolled.add(enrolled)
    major.save()

def linkMajorAndCategoryHelper(major_pk, category_pk):
    major = Major.objects.get(pk=major_pk)
    category = Category.objects.get(pk=category_pk)
    category.major.add(major)
    category.save()

def linkCategoryAndSubcategoryHelper(category_pk, subcategory_pk):
    category = Category.objects.get(pk=category_pk)
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    subcategory.categories.add(category) 
    subcategory.save()

def linkSubcategoryAndRequirementHelper(subcategory_pk, requirement_pk):
    subcategory = SubCategory.objects.get(pk=subcategory_pk)
    requirement = Requirement.objects.get(pk=requirement_pk)
    requirement.subcategories.add(subcategory) 
    requirement.save()

def linkRequirementAndCourseHelper(requirement_pk, course_pk):
    requirement = Requirement.objects.get(pk=requirement_pk)
    course = Course.objects.get(pk=course_pk)
    course.requirements.add(requirement)
    course.save()

def linkCourseAndPrereqHelper(course_pk, prereq_pk):
    course = Course.objects.get(pk=course_pk)
    prereq = Prereq.objects.get(pk=prereq_pk)
    prereq.courses.add(course)
    prereq.save()

def linkCourseAndApHelper(course_pk, ap_pk):
    course = Course.objects.get(pk=course_pk)
    test = ApCredit.objects.get(pk=ap_pk)
    test.courses.add(course)
    test.save()

