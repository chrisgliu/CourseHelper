from .courseslist import *

def deleteStudent(username):
    student = getStudent(username)
    student.delete()

def deleteEnrollKey(username):
    enroll_key = getEnrollKey(username)
    enroll_key.delete()

def deleteMajor(username, major):
    major = getMajor(username, major)
    major.delete()

def deleteCategory(username, major, category):
    category = getCategory(username, major, category)
    category.delete()

def deleteSubcategory(username, major, category, subcategory):
    subcategory = getSubCategory(username, major, category, subcategory)
    subcategory.delete()

def deleteRequirement(username, major, category, subcategory, requirement):
    requirement = getRequirement(username, major, category, subcategory, requirement)
    requirement.delete()

def deleteCourse(username, major, category, subcategory, requirement, course):
    coursse = getCourse(username, major, category, subcategory, requirement, course)
    course.delete()

def deletePrereq(username, major, category, subcategory, requirement, course, prereq):
    prereq = getPrereq(username, major, category, subcategory, requirement, course, prereq)
    prereq.delete()

def deleteTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax):
    test = getTest(username, major, category, subcategory, requirement, course, test, scoremin, scoremax)
    test.delete()

