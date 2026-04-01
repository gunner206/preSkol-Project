from django.shortcuts import render, redirect, get_object_or_404
from department.models import Department
from home_auth.models import CustomUser
from .models import Teacher
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teacher_list': teachers})

@login_required
def add_teacher(request):
    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = Department.objects.filter(id=department_id).first() if department_id else None
        
        # Capture the ID from the form to use for the user and the teacher_id field
        t_id = request.POST.get('id') or request.POST.get('username')

        # --- NEW: Check if the user already exists to prevent the 500 crash ---
        if CustomUser.objects.filter(username=t_id).exists():
            messages.error(request, f'A teacher or user with ID "{t_id}" already exists. Please use a unique ID.')
            return redirect('add_teacher')
        # ----------------------------------------------------------------------

        user = CustomUser.objects.create_user(
            username=t_id,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            is_teacher=True
        )

        Teacher.objects.create(
            user=user,
            teacher_id=t_id, 
            department=department,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            mobile_number=request.POST.get('mobile_number'),
            joining_date=request.POST.get('joining_date'),
            experience=request.POST.get('experience', '0 Years') # ADDED THIS LINE
        )
        messages.success(request, 'Teacher added successfully.')
        return redirect('teacher_list')
    
    departments = Department.objects.all()
    return render(request, 'teachers/add-teacher.html', {'departments': departments})

@login_required
def teacher_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})

@login_required
def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = Department.objects.filter(id=department_id).first() if department_id else None

        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.experience = request.POST.get('experience', '0 Years') # ADDED THIS LINE
        teacher.department = department 
        teacher.save()
        
        messages.success(request, 'Teacher updated successfully.')
        return redirect('teacher_list')
    
    departments = Department.objects.all()
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher, 'departments': departments})

@login_required
def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    user = teacher.user # Target the user associated with this teacher
    teacher.delete()
    if user:
        user.delete() # Deleting the CustomUser prevents database bloat
        
    messages.success(request, 'Teacher deleted successfully.')
    return redirect('teacher_list')

