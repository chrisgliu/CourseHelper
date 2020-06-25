from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Major, Category, SubCategory, Requirement, Course, Prereq

# Register your models here.

# importing and exporting data
class MajorResource(resources.ModelResource):
    class Meta:
        model = Major
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory
class RequirementResource(resources.ModelResource):
    class Meta:
        model = Requirement
class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
class PrereqResource(resources.ModelResource):
    class Meta:
        model = Prereq

# related name relations
class PrereqsInline(admin.StackedInline):
    model = Prereq.courses.through
class CourseInline(admin.StackedInline):
    model = Course.requirements.through
class ReqInLine(admin.StackedInline):
    model = Requirement.subcategories.through
class SubCategoryInLine(admin.StackedInline):
    model = SubCategory.categories.through

# admin
@admin.register(Prereq)
class PrereqAdmin(ImportExportModelAdmin):
    resource_class = PrereqResource
    filter_horizontal = ("courses",)

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    resource_class = CourseResource
    inlines = [PrereqsInline]
    filter_horizontal = ("requirements",)

@admin.register(Requirement)
class ReqAdmin(ImportExportModelAdmin):
    resource_class = RequirementResource
    inlines = [CourseInline];
    filter_horizontal = ("subcategories",)

@admin.register(SubCategory)
class SubCategoryAdmin(ImportExportModelAdmin):
    resource_class = SubCategoryResource
    inlines = [ReqInLine];
    filter_horizontal = ("categories",)

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    inlines = [SubCategoryInLine];

class MajorAdmin(ImportExportModelAdmin):
    resource_class = MajorResource
admin.site.register(Major, MajorAdmin)