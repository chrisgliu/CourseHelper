from ..models import *

def createStudent(firstname, lastname, username):
    new_student = Student(firstname=firstname, lastname=lastname, username=username)
    new_student.save()
    return new_student.pk

def createEnrollKey(username):
    new_key = Enrolled(enrolled=username)
    new_key.save()
    return new_key.pk

def createMajor(major):
    new_major = Major(major=major)
    new_major.save()
    return new_major.pk

def createCategory(category):
    new_category = Category(category=category)
    new_category.save()
    return new_category.pk

def createSubcategory(subcategory, note):
    new_subcategory = SubCategory(subcategory=subcategory, note=note)
    new_subcategory.save()
    return new_subcategory.pk

def createRequirement(requirement, credit):
    new_requirement = Requirement(requirement=requirement, credit=credit)
    new_requirement.save()
    return new_requirement.pk

def createCourse(course, credit):
    new_course = Course(course=course, credit=credit)
    new_course.save()
    return new_course.pk

def createPrereq(prereq):
    new_prereq = Prereq(prereq=prereq)
    new_prereq.save()
    return new_prereq.pk

def createAp(test, scoremin, scoremax):
    new_test = ApCredit(test=test, scoremin=scoremin, scoremax=scoremax)
    new_test.save()
    return new_test.pk


