from django.shortcuts import render , redirect
from .models import Department
from teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Create your views here.

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

@login_required
def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')


        Department.objects.create(
            name=name,
            description=description
        )
        return redirect('department_list')
    
    teachers = Teacher.objects.all()
    return render(request, 'departments/add_department.html', {'teachers': teachers})

@login_required
def edit_department(request, department_id):
    department = Department.objects.get(id=department_id)
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.save()
        return redirect('department_list')
    
    teachers = Teacher.objects.all()
    return render(request, 'departments/edit_department.html', {'department': department, 'teachers': teachers})
