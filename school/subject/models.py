from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    department = models.ForeignKey('department.Department', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.department.name})"