from django.shortcuts import render, redirect, get_object_or_404
from department.models import Department # Fixed broken import
from .models import Subject
from teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden



@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'subjects': subjects})    

@login_required
def add_subject(request):
    if request.user.is_student:
        return HttpResponseForbidden("Accès refusé.")
    if request.method == 'POST':
        name = request.POST.get('name')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        description = request.POST.get('description')

        department = Department.objects.filter(id=department_id).first() if department_id else None
        teacher = Teacher.objects.filter(id=teacher_id).first() if teacher_id else None

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
    if not request.user.is_admin or not request.user.is_teacher:
        return HttpResponseForbidden("Accès refusé.")
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        subject.name = request.POST.get('name')
        department_id = request.POST.get('department')
        teacher_id = request.POST.get('teacher')
        subject.description = request.POST.get('description')

        subject.department = Department.objects.filter(id=department_id).first() if department_id else None
        subject.teacher = Teacher.objects.filter(id=teacher_id).first() if teacher_id else None

        subject.save()
        return redirect('subject_list')
    
    departments = Department.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'subjects/edit_subject.html', {'subject': subject, 'departments': departments, 'teachers': teachers})

@login_required
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    messages.success(request, 'Subject deleted successfully.')
    return redirect('subject_list')