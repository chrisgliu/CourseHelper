from django.db import models

# Create your models here.

# --- MAJOR --- 
# holds the name of a major
class Major(models.Model):
    major = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.major}"
    class Meta:
        verbose_name_plural = "1. Majors"

# --- CATEGORY ---
# holds the name of a core section of a major ex: General Education
# if a section is deleted, all corresponding data is deleted
class Category(models.Model):
    category = models.CharField(max_length=64)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="categories")
    def __str__(self):
        return f"{self.category}"
    class Meta:
        verbose_name_plural = "2. Categories"

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
        verbose_name_plural = "3. Sub Categories"

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
        verbose_name_plural = "4. Requirements"

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
        verbose_name_plural = "5. Courses"

# --- PREREQ ---
# holds the name of a prereq, probably a course
# enables accessing the courses that require this prereq and accessing the prereqs required for a course
class Prereq(models.Model):
    prereq = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, blank=True, related_name="prereqs")
    def __str__(self):
        return f"{self.prereq}"
    class Meta:
        verbose_name_plural = "6. Prereqs"

# --- APCREDIT ---
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
        verbose_name_plural = "7. ApCredit"