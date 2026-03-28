from django.shortcuts import render , redirect
from .models import Department
from .models import Subject
from teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.
@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})    

@login_required
def add_subject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        description = request.POST.get('description')

        department = Department.objects.get(id=department_id) if department_id else None
        teacher = Teacher.objects.get(id=teacher_id) if teacher_id else None

        Subject.objects.create(
            name=name,
            department=department,
            teacher=teacher,
            description=description
        )
        return redirect('subject_list')
    
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'subjects/add_subject.html', {'departments': departments, 'teachers': teachers})

