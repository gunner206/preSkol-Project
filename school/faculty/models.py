from django.db import models

# Create your models here.

from django.db import models

class Holiday(models.Model):
    HOLIDAY_TYPES = (
        ('Public Holiday', 'Public Holiday'),
        ('School Holiday', 'School Holiday'),
        ('Term Break', 'Term Break'),
        ('Exam Break', 'Exam Break'),
    )

    name = models.CharField(max_length=200)
    holiday_type = models.CharField(max_length=50, choices=HOLIDAY_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"


class Exam(models.Model):
    name = models.CharField(max_length=100, help_text="e.g., Mid Term, Final Exams, Unit Test")
    exam_class = models.CharField(max_length=50, help_text="e.g., Class 10, Class A")
    # If you have a Subject model, uncomment the line below and delete the CharField
    # subject = models.ForeignKey('subject.Subject', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        ordering = ['exam_date', 'start_time']

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.exam_class})"


class TimeTable(models.Model):
    # Assuming your teacher model is named 'Teacher' inside the 'teacher' app
    teacher = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='timetables')
    class_name = models.CharField(max_length=50, help_text="e.g., Class 10 A")
    
    # If you have a Subject model, uncomment the line below and delete the CharField
    # subject = models.ForeignKey('subject.Subject', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['date', 'start_time']
        verbose_name = "Time Table"
        verbose_name_plural = "Time Tables"

    def __str__(self):
        return f"{self.class_name} | {self.subject} | {self.teacher}"