from django.db import models


# Create your models here.


# --- STUDENT --- 
# used to link data to USER
class Student(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    username = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name_plural = "1. Students"


# --- ENROLLED ---
# links student to the rest of the data
# holds enrollment status
# if an enrolled student is deleted, all corresponding data is deleted
class Enrolled(models.Model):
    enrolled = models.BooleanField(default=True)
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrolled")

    class Meta:
        verbose_name_plural = "2. Enrolled"


# --- MAJOR ---
# holds the name of a major
# enables accessing the students of a major and accessing the major of a student
class Major(models.Model):
    major = models.CharField(max_length=64)
    enrolled = models.ManyToManyField(Enrolled, blank=False, related_name="majors")

    def __str__(self):
        return f"{self.major}"

    class Meta:
        verbose_name_plural = "3. Majors"



# --- CATEGORY ---
# holds the name of a core section of a major ex: General Education
# enables accessing the major of a core section and accessing the core section of a major
class Category(models.Model):
    category = models.CharField(max_length=64)
    major =  models.ManyToManyField(Major, blank=False, related_name="categories")

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name_plural = "4. Categories"


# --- SUBCATEGORY ---
# holds the name of a sub category within a core section ex: Natural Sciences
# enables accessing the core section of a sub category and accessing the sub category of a core section
class SubCategory(models.Model):
    subcategory = models.CharField(max_length=64)
    note = models.TextField()
    categories = models.ManyToManyField(Category, blank=False, related_name="subcategories")

    def __str__(self):
        return f"{self.subcategory}"

    class Meta:
        verbose_name_plural = "5. Sub Categories"


# --- REQUIREMENT ---
# holds the name of a requirement for a subcategory and its correponding credit target
# enables accessing the sub category of a requirement and accessing the requirement of a sub category
class Requirement(models.Model):
    requirement = models.CharField(max_length=64)
    credit = models.IntegerField(default=1)
    subcategories = models.ManyToManyField(SubCategory, blank=False, related_name="requirements")

    def __str__(self):
        return f"{self.requirement}"

    class Meta:
        verbose_name_plural = "6. Requirements"


# --- COURSE ---
# holds the name of a course and its correponding credit
# enables accessing the requirements fulfilled by a course and accessing the courses that can fulfill a requirement
class Course(models.Model):
    course = models.CharField(max_length=64)
    credit = models.IntegerField(default=1)
    requirements = models.ManyToManyField(Requirement, blank=False, related_name="courses")

    def __str__(self):
        return f"{self.course}"

    class Meta:
        verbose_name_plural = "7. Courses"


# --- PREREQ ---
# holds the name of a prereq, probably a course
# enables accessing the courses that require this prereq and accessing the prereqs required for a course
class Prereq(models.Model):
    prereq = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, blank=True, related_name="prereqs")

    def __str__(self):
        return f"{self.prereq}"

    class Meta:
        verbose_name_plural = "8. Prereqs"


# --- AP CREDIT ---
# holds the name of an ap test and a score range
# enables accessing the courses that are fulfilled with this ap score and accessing the ap scores required for a course
class ApCredit(models.Model):
    test = models.CharField(max_length=64)
    scoremin = models.IntegerField(default=3)
    scoremax = models.IntegerField(default=3)
    courses = models.ManyToManyField(Course, blank=True, related_name="apcredits")

    def __str__(self):
        return f"{self.test}:{self.scoremin}-{self.scoremax}"

    class Meta:
        verbose_name_plural = "9. ApCredit"
