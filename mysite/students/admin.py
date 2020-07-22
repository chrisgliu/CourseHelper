from django.contrib import admin
from .models import *

# Register your models here.

# --- related name relations ---

class CourseInline(admin.StackedInline):
    model = Course.semesters.through


class YearInline(admin.StackedInline):
    model = Year.enrolled.through


class MajorInline(admin.StackedInline):
    model = Major.enrolled.through

# --- admin register ---
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    filter_horizontal = ("semesters",)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    filter_horizontal = ("years",)

@admin.register(AP)
class APAdmin(admin.ModelAdmin):
    filter_horizontal = ("years",)


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    filter_horizontal = ("enrolled",)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    filter_horizontal = ("enrolled",)


@admin.register(Enrolled)
class EnrolledAdmin(admin.ModelAdmin):
    inlines = [YearInline, MajorInline]


admin.site.register(Student)
