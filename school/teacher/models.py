from django.db import models
from home_auth.models import CustomUser

class Teacher(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'), 
        ('Female', 'Female')
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    joining_date = models.DateField()
    
    # ADDED THIS LINE:
    experience = models.CharField(max_length=50, default="0 Years") 
    
    teacher_image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    department = models.ForeignKey('department.Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"