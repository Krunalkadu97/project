from django.contrib import admin
from .models import Course,Course_Single
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_diaplay=('name','mentor')
admin.site.register(Course,CourseAdmin)
class Course_SingleAdmin(admin.ModelAdmin):
    list_diaplay=('name','mentor','category','student','price','shift')
admin.site.register(Course_Single,Course_SingleAdmin)
