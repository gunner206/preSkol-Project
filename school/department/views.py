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
        head_of_department_id = request.POST.get('head_of_department')
        description = request.POST.get('description')

        head_of_department = Teacher.objects.get(id=head_of_department_id) if head_of_department_id else None

        Department.objects.create(
            name=name,
            head_of_department=head_of_department,
            description=description
        )
        return redirect('department_list')
    
    teachers = Teacher.objects.all()
    return render(request, 'departments/add_department.html', {'teachers': teachers})