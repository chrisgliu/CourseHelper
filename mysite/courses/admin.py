from django.contrib import admin

from .models import Major, Categories, Requirements, CourseOptions, Prerequisites
# Register your models here.

# class PassengerInline(admin.StackedInline):
#     model = Passenger.flights.through
#     extra = 1
# class FlightAdmin(admin.ModelAdmin):
#     inlines = [PassengerInline]
# class PassengerAdmin(admin.ModelAdmin):
#     filter_horizontal = ("flights",)

admin.site.register(Major)
admin.site.register(Categories)
admin.site.register(Requirements)
admin.site.register(CourseOptions)
admin.site.register(Prerequisites)