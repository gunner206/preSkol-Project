from django.db import models
from home_auth.models import CustomUser

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    teacher_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    joining_date = models.DateField()
    teacher_image = models.ImageField(upload_to='teachers/', blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"
