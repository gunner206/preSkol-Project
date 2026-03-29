from django.shortcuts import render , redirect
from department.models import Department
from teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'students/student.html', {'teachers': teachers})

@login_required
def add_teacher(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_id = request.POST.get('teacher_id')
        department_id = request.POST.get('department')

        department = Department.objects.get(id=department_id) if department_id else None

        Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            teacher_id=teacher_id,
            department=department
        )
        messages.success(request, 'Teacher added successfully.')
        return redirect('teacher_list')
    departments = Department.objects.all()
    return render(request, 'students/add_student.html', {'departments': departments})


def teacher_viw(request):
    return render(request, 'students/students.html')
def teacher_edit(request):
    return render(request, 'students/edit_student.html')

def teacher_delete(request):
    return render(redirect, 'students/students.html')
