from django.contrib import admin
from .models import Holiday, Exam, TimeTable, Result

# Register your models here.

admin.site.register(Holiday)
admin.site.register(Exam)
admin.site.register(TimeTable)
admin.site.register(Result)
