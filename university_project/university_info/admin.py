from django.contrib import admin
from university_info.models import *

# Register your models here.
# admin.site.register(College)
admin.site.register(Courses)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subjects)
admin.site.register(Role)


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'name', 'address']
