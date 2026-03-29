# student/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Student, Parent
from django.contrib import messages

def student_list(request):
    # i need to pass student_list to the frontend
    student_list = dict()
    if request.method == 'GET':
        students = Student.objects.all()
        if students:
            student_list = students.values()
    return render(request, 'students/students.html', {'student_list': student_list})

def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        # Récupérer les données du parent
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
    
        parent = Parent.objects.create(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )
        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            student_id=student_id,
            gender=gender,
            date_of_birth=date_of_birth,
            student_class=student_class,
            joining_date=joining_date,
            mobile_number=mobile_number,
            admission_number=admission_number,
            section=section,
            student_image=student_image,
            parent=parent
        )
        messages.success(request, 'Student added Successfully')
        return redirect('student_list')
    else:
        return render(request, 'students/add-student.html')
    
def edit_student(request, student_id):
    if not student_id:
        return render(request, "students/students.html")
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # student_id = request.POST.get('student_id')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        student_class = request.POST.get('student_class')
        joining_date = request.POST.get('joining_date')
        mobile_number = request.POST.get('mobile_number')
        admission_number = request.POST.get('admission_number')
        section = request.POST.get('section')
        student_image = request.FILES.get('student_image')

        # Récupérer les données du parent
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        father_email = request.POST.get('father_email')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        mother_mobile = request.POST.get('mother_mobile')
        mother_email = request.POST.get('mother_email')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')

        # removing old parent
        student = Student.objects.get(student_id = student_id)
        parent_id = student.parent.id

        Parent.objects.filter(id = parent_id).update(
            father_name=father_name,
            father_occupation=father_occupation,
            father_mobile=father_mobile,
            father_email=father_email,
            mother_name=mother_name,
            mother_occupation=mother_occupation,
            mother_mobile=mother_mobile,
            mother_email=mother_email,
            present_address=present_address,
            permanent_address=permanent_address
        )
        
        student.first_name=first_name
        student.last_name=last_name
        # student_id=student_id,
        student.gender=gender
        student.date_of_birth=date_of_birth
        student.student_class=student_class
        student.joining_date=joining_date
        student.mobile_number=mobile_number
        student.admission_number=admission_number
        student.section=section
        student.student_image=student_image
        student.save()
        # parent=parent

        messages.success(request, 'Student Updated Succesfuly')
        # return redirect('view_student', student_id=student_id)
        return redirect('student_list')
    else:
        return render(request, 'students/edit-student.html')
    
def view_student(request, student_id):
    if student_id:
        student = Student.objects.get(student_id = student_id)
        return render(request, 'students/student-details.html', {'student':student})
    else:
        return redirect('student_list')

def delete_student(request, student_id):
    try:
        student = Student.objects.filter(student_id = student_id).first()
        student.delete()
        messages.success(request, "Student Deleted succesfuly")
        return redirect('student_list')
    except Exception:
        messages.error(request, "Error happend when Deleting")
        return redirect('student_list')
