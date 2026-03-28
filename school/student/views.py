# student/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Parent
from django.contrib import messages

def student_list(request):
    # i need to pass student_list to the frontend
    student_list = []
    if request.method == 'GET':
        students = Student.objects.all()
        for student in students:
            current_student = {}
            current_student.first_name = student.first_name
            current_student.last_name = student.last_name
            current_student.student_id = student.student_id
            current_student.gender = student.gender
            current_student.date_of_birth = student.student_id
            current_student.student_class = student.student_class
            current_student.joining_date = student.joining_date
            current_student.mobile_number = student.mobile_number
            current_student.admission_number = student.admission_number
            current_student.section = student.section
            current_student.student_image = student.student_image
            student_list.append(current_student)

    return render(request, 'students/students.html', {'student_list' : student_list})

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
    return render(request, 'students/edit-student.html')
def view_student(request, student_id):
    return render(request, 'students/student-details.html')
def delete_student(request, student_id):
    return redirect('student_list')