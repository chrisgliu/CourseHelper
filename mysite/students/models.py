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

# --- YEAR --- 
# holds the year ex: 2020
# enables accessing the students of a Year and accessing the Year of a student
class Year(models.Model):
    year = models.CharField(max_length=5)
    enrolled = models.ManyToManyField(Enrolled, blank=False, related_name="years")
    class Meta:
        verbose_name_plural = "4. Years"

# --- SEMESTER --- 
# holds the semester ex: autumn
# enables accessing the year of a semester and accessing the semester of a year
class Semester(models.Model):
    semester = models.CharField(max_length=64)
    years = models.ManyToManyField(Year, blank=False, related_name="semesters")
    class Meta:
        verbose_name_plural = "5. Semesters"

# --- COURSE --- 
# holds the name of the course
# enables accessing the semester of a course and accessing the course of a semester
class Course(models.Model):
    course = models.CharField(max_length=64)
    semesters = models.ManyToManyField(Semester, blank=False, related_name="courses")
    class Meta:
        verbose_name_plural = "6. Courses"
