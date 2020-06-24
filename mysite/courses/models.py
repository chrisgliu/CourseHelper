from django.db import models

# Create your models here.

class Major(models.Model):
    major = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.major}"

class Categories(models.Model):
    category = models.CharField(max_length=64)
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="category")
    def __str__(self):
        return f"Major:{self.major}, Category:{self.category}"

class Requirements(models.Model):
    requirement = models.CharField(max_length=64)
    creditrange = models.IntegerField(default=1)
    numcoursesneeded = models.IntegerField(default=1)
    category = models.ManyToManyField(Categories, blank=False, related_name="requirement")
    def __str__(self):
        return f"Category:{self.category}, Req:{self.requirement}"

class CourseOptions(models.Model):
    course = models.CharField(max_length=64)
    credithour = models.IntegerField(default=1)
    requirement = models.ManyToManyField(Requirements, blank=False, related_name="course")
    def __str__(self):
        return f"Req:{self.requirement}, Course:{self.course}"

class Prerequisites(models.Model):
    prereq = models.CharField(max_length=64)
    course = models.ManyToManyField(CourseOptions, blank=True, related_name="prereq")
    def __str__(self):
        return f"Course:{self.course}, PreReq:{self.prereq}"
