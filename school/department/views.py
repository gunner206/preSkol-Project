from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/departments.html', {'departments': departments})

@login_required
def add_department(request):
    if not request.user.is_admin:
        return HttpResponseForbidden("Accès refusé. Réservé aux enseignants.")
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        Department.objects.create(
            name=name,
            description=description
        )
        messages.success(request, 'Department added successfully.')
        return redirect('department_list')
    
    return render(request, 'departments/add_department.html')

@login_required
def edit_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    if not request.user.is_admin:
        return HttpResponseForbidden("Accès refusé. Réservé aux enseignants.")
    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.save()
        messages.success(request, 'Department updated successfully.')
        return redirect('department_list')
    
    return render(request, 'departments/edit_department.html', {'department': department})

# --- NEW VIEW FOR DELETING ---
@login_required
def delete_department(request, department_id):
    department = get_object_or_404(Department, id=department_id)
    department.delete()
    messages.success(request, 'Department deleted successfully.')
    return redirect('department_list')