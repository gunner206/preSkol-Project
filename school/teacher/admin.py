from django.contrib import admin
from .models import Teacher
from department.models import Department
from subject.models import Subject
# Register your models here. 
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name' )
    search_fields = ('first_name', 'last_name' )
    list_filter = ('department',)
    

