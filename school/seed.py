import os
import django

# 1. Setup Django Environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "school.settings")
django.setup()

# 2. Import all your models
from home_auth.models import CustomUser
from teacher.models import Teacher
from student.models import Parent, Student
from department.models import Department
from subject.models import Subject
from faculty.models import TimeTable, Exam, Holiday

print("Creating Users (Passwords are hashed automatically as 'password123')...")
admin_user = CustomUser.objects.create_superuser(
    username='admin@school.com', email='admin@school.com', password='password123',
    first_name='Super', last_name='Admin', is_admin=True
)

t1_user = CustomUser.objects.create_user(
    username='teacher1@school.com', email='teacher1@school.com', password='password123',
    first_name='Alan', last_name='Turing', is_teacher=True
)

t2_user = CustomUser.objects.create_user(
    username='teacher2@school.com', email='teacher2@school.com', password='password123',
    first_name='Marie', last_name='Curie', is_teacher=True
)

s1_user = CustomUser.objects.create_user(
    username='student1@school.com', email='student1@school.com', password='password123',
    first_name='John', last_name='Smith', is_student=True
)

print("Creating Teachers...")
# Using a try-except to handle your custom 'experience' field safely
teacher1_data = {
    'user': t1_user, 'first_name': 'Alan', 'last_name': 'Turing', 'teacher_id': 'T-001',
    'gender': 'Male', 'date_of_birth': '1985-06-23', 'mobile_number': '+212600000001', 'joining_date': '2020-09-01'
}
try:
    t1 = Teacher.objects.create(experience='5 Years', **teacher1_data)
except TypeError:
    t1 = Teacher.objects.create(**teacher1_data)

teacher2_data = {
    'user': t2_user, 'first_name': 'Marie', 'last_name': 'Curie', 'teacher_id': 'T-002',
    'gender': 'Female', 'date_of_birth': '1990-11-07', 'mobile_number': '+212600000002', 'joining_date': '2021-09-01'
}
try:
    t2 = Teacher.objects.create(experience='8 Years', **teacher2_data)
except TypeError:
    t2 = Teacher.objects.create(**teacher2_data)


print("Creating Parents & Students...")
parent = Parent.objects.create(
    father_name='Robert Smith', father_occupation='Engineer', father_mobile='+212611111111', father_email='robert.smith@email.com',
    mother_name='Sarah Smith', mother_occupation='Doctor', mother_mobile='+212622222222', mother_email='sarah.smith@email.com',
    present_address='123 Main Street', permanent_address='123 Main Street'
)

student_data = {
    'first_name': 'John', 'last_name': 'Smith', 'student_id': 'S-1001', 'gender': 'Male',
    'date_of_birth': '2010-05-14', 'student_class': 'Class 10', 'joining_date': '2025-09-01',
    'mobile_number': '+212633333333', 'admission_number': 'ADM-2025-01', 'section': 'A', 'parent': parent
}
# Safely link CustomUser if you added the user OneToOneField to the Student model
try:
    Student.objects.create(user=s1_user, **student_data)
except TypeError:
    Student.objects.create(**student_data)


print("Creating Departments & Subjects...")
d1 = Department.objects.create(name='Mathematics', description='Math Dept', head_of_department=t1)
d2 = Department.objects.create(name='Science', description='Science Dept', head_of_department=t2)

sub1 = Subject.objects.create(name='Algebra', description='Advanced Algebra', department=d1, teacher=t1)
sub2 = Subject.objects.create(name='Physics', description='Thermodynamics', department=d2, teacher=t2)


print("Creating Time Table, Exams, and Holidays...")
TimeTable.objects.create(class_name='Class 10 A', subject='Algebra', date='2026-04-06', start_time='08:00:00', end_time='10:00:00', teacher=t1)
TimeTable.objects.create(class_name='Class 10 A', subject='Physics', date='2026-04-06', start_time='10:30:00', end_time='12:30:00', teacher=t2)

Exam.objects.create(name='Mid-Term Math', exam_class='Class 10 A', subject='Algebra', exam_date='2026-05-15', start_time='09:00:00', end_time='12:00:00')

Holiday.objects.create(name='Spring Break', holiday_type='Term Break', start_date='2026-04-20', end_date='2026-04-26', description='One week break.')

print("✅ Database successfully seeded!")