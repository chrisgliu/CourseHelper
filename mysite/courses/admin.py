from django.contrib import admin

from .models import Major, Category, SubCategory, Requirement, Course, Prereq
# Register your models here.

class PrereqsInline(admin.StackedInline):
    model = Prereq.courses.through

class PrereqAdmin(admin.ModelAdmin):
    filter_horizontal = ("courses",)

class CourseInline(admin.StackedInline):
    model = Course.requirements.through

class CourseAdmin(admin.ModelAdmin):
    inlines = [PrereqsInline]
    filter_horizontal = ("requirements",)

class ReqInLine(admin.StackedInline):
    model = Requirement.subcategories.through

class ReqAdmin(admin.ModelAdmin):
    inlines = [CourseInline];
    filter_horizontal = ("subcategories",)

class SubCategoryInLine(admin.StackedInline):
    model = SubCategory.categories.through

class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [ReqInLine];
    filter_horizontal = ("categories",)

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInLine];

admin.site.register(Major)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Requirement, ReqAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Prereq, PrereqAdmin)