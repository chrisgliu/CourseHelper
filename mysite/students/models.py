from django.db import models

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    class Meta:
        verbose_name_plural = "1. Students"

class Enrolled(models.Model):
    enrolled = models.BooleanField(default=True)
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrolled")
    class Meta:
        verbose_name_plural = "2. Enrolled"

class Major(models.Model):
    major = models.CharField(max_length=64)
    enrolled = models.ManyToManyField(Enrolled, blank=False, related_name="majors")
    def __str__(self):
        return f"{self.major}"
    class Meta:
        verbose_name_plural = "3. Majors"

class Year(models.Model):
    year = models.CharField(max_length=5)
    enrolled = models.ManyToManyField(Enrolled, blank=False, related_name="years")
    class Meta:
        verbose_name_plural = "4. Years"

class Semester(models.Model):
    semester = models.CharField(max_length=64)
    years = models.ManyToManyField(Year, blank=False, related_name="semesters")
    class Meta:
        verbose_name_plural = "5. Semesters"

class Course(models.Model):
    course = models.CharField(max_length=64)
    semesters = models.ManyToManyField(Semester, blank=False, related_name="courses")
    class Meta:
        verbose_name_plural = "6. Courses"
