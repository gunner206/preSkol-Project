from django.shortcuts import render , redirect , get_object_or_404
from department.models import Department
from home_auth.models import CustomUser
from teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teacher_list': teachers})

@login_required
def add_teacher(request):
    if request.method == 'POST':
        department_id = request.POST.get('department')
        department = Department.objects.get(id=department_id) if department_id else None
        
        user = CustomUser.objects.create_user(
            username=request.POST.get('teacher_id'),
            password=CustomUser.objects.make_random_password(),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            is_teacher=True
        )

        Teacher.objects.create(
            user=user,
            department=department,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            teacher_id=request.POST.get('teacher_id'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            mobile_number=request.POST.get('mobile_number'),
            joining_date=request.POST.get('joining_date')
        )
        messages.success(request, 'Teacher added successfully.')
        return redirect('teacher_list')
    departments = Department.objects.all()
    return render(request, 'teachers/add-teacher.html', {'departments': departments})

@login_required
def teacher_view(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teachers/teachers.html', {'teacher': teacher})

@login_required
def teacher_edit(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.gender = request.POST.get('gender')
        teacher.date_of_birth = request.POST.get('date_of_birth')
        teacher.mobile_number = request.POST.get('mobile_number')
        teacher.joining_date = request.POST.get('joining_date')
        teacher.save()
        messages.success(request, 'Teacher updated successfully.')
        return redirect('teacher_list')
    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher})

@login_required
def teacher_delete(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    messages.success(request, 'Teacher deleted successfully.')
    return redirect('teacher_list')