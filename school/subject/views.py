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

@login_required
def edit_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        subject.description = request.POST.get('description')

        subject.department = Department.objects.get(id=department_id) if department_id else None
        subject.teacher = Teacher.objects.get(id=teacher_id) if teacher_id else None

        subject.save()
        return redirect('subject_list')
    
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'subjects/edit_subject.html', {'subject': subject, 'departments': departments, 'teachers': teachers})