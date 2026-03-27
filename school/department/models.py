from django.db import models
from teacher.models import Teacher

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name