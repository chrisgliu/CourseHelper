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
        verbose_name_plural = "1. Course Students"


# --- ENROLLED ---
# links student to the rest of the data
# holds enrollment status
# if an enrolled student is deleted, all corresponding data is deleted
class Enrolled(models.Model):
    enrolled = models.BooleanField(default=True)
    students = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrolled")

    def __str__(self):
        the_student = Student.objects.get(pk=self.students.pk)
        return str(the_student)

    class Meta:
        verbose_name_plural = "2. Course Enrolled"


# --- MAJOR ---
# holds the name of a major
# enables accessing the students of a major and accessing the major of a student
class Major(models.Model):
    major = models.CharField(max_length=64)
    enrolled = models.ManyToManyField(Enrolled, blank=False, related_name="majors")

    def __str__(self):
        return f"{self.major}"

    class Meta:
        verbose_name_plural = "3. Course Majors"


# --- YEAR ---
# holds the year ex: 2020
# enables accessing the students of a Year and accessing the Year of a student
class Year(models.Model):
    year = models.CharField(max_length=6)
    enrolled = models.ManyToManyField(Enrolled, blank=False, related_name="years")

    def __str__(self):
        return f"{self.year}"

    class Meta:
        verbose_name_plural = "4. Course Years"

# -- AP ---
# holds test name and score number
class AP(models.Model):
    test = models.CharField(max_length=64)
    score = models.IntegerField(blank=False)
    years = models.ManyToManyField(Year, blank=False, related_name="ap")
    def __str__(self):
        return f"{self.test}/{self.score}"

    class Meta:
        verbose_name_plural = "7. Course AP"


# --- SEMESTER ---
# holds the semester ex: autumn
# enables accessing accessing the semester of a year
class Semester(models.Model):
    semester = models.CharField(max_length=64)
    years = models.ManyToManyField(Year, blank=False, related_name="semesters")
    def __str__(self):
        the_year = Year.objects.get(pk=self.years.first().pk)
        return f"{the_year.year}/{self.semester}"

    class Meta:
        verbose_name_plural = "5. Course Semesters"


# --- COURSE ---
# holds the name of the course
# enables accessing the semester of a course and accessing the course of a semester
class Course(models.Model):
    course = models.CharField(max_length=64)
    semesters = models.ManyToManyField(Semester, blank=False, related_name="courses")

    def __str__(self):
        return f"{self.course}"

    class Meta:
        verbose_name_plural = "6. Course Courses"
