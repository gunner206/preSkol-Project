from django.contrib import admin
from .models import Teacher
from department.models import Department
from subject.models import Subject
# Register your models here. 
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'teacher_id')
    search_fields = ('first_name', 'last_name', 'teacher_id')
    list_filter = ('department',)
    

