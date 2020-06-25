from django.db import models

# Create your models here.

class Major(models.Model):
    major = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.major}"
    class Meta:
        verbose_name_plural = "1. Majors"

class Category(models.Model):
    category = models.CharField(max_length=64)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="categories")
    def __str__(self):
        return f"{self.category}"
    class Meta:
        verbose_name_plural = "2. Categories"

class SubCategory(models.Model):
    subcategory = models.CharField(max_length=64)
    note = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, blank=False, related_name="subcategories")
    def __str__(self):
        return f"{self.subcategory}"
    class Meta:
        verbose_name_plural = "3. Sub Categories"

class Requirement(models.Model):
    requirement = models.CharField(max_length=64)
    credit = models.IntegerField(default=1)
    subcategories = models.ManyToManyField(SubCategory, blank=False, related_name="requirements")
    def __str__(self):
        return f"{self.requirement}"
    class Meta:
        verbose_name_plural = "4. Requirements"

class Course(models.Model):
    course = models.CharField(max_length=64)
    credit = models.IntegerField(default=1)
    requirements = models.ManyToManyField(Requirement, blank=False, related_name="courses")
    def __str__(self):
        return f"{self.course}"
    class Meta:
        verbose_name_plural = "5. Courses"

class Prereq(models.Model):
    prereq = models.CharField(max_length=64)
    courses = models.ManyToManyField(Course, blank=True, related_name="prereqs")
    def __str__(self):
        return f"{self.prereq}"
    class Meta:
        verbose_name_plural = "6. Prereqs"

class ApCredit(models.Model):
    test = models.CharField(max_length=64)
    scores = models.IntegerField(default=3)
    courses = models.ManyToManyField(Course, blank=True, related_name="apcredits")
    def __str__(self):
        return f"{self.test}:{self.scores}"
    class Meta:
        verbose_name_plural = "6. ApCredit"