from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Holiday, Exam, TimeTable, Result
from teacher.models import Teacher
from student.models import Student
from subject.models import Subject
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'authentication/login.html')

# def dashboard(request):
#     return render(request, 'Home/admin-dashboard.html')


def exam(request):
    exams = Exam.objects.all()
    return render(request, 'management/exam.html', {'exam_list' : exams})
def holiday(request):
    holidays = Holiday.objects.all()
    return render(request, 'management/holiday.html', {'holiday_list' : holidays})

def time_table(request):
    timeTables = TimeTable.objects.all()
    events = []

    for tt in timeTables:
        start_datetime = f"{tt.date.isoformat()}T{tt.start_time.strftime('%H:%M:%S')}"
        end_datetime = f"{tt.date.isoformat()}T{tt.end_time.strftime("%H:%M:%S")}"

        events.append({
            'title': f"{tt.subject} ({tt.class_name})",
            'start': start_datetime,
            'end' : end_datetime,
            'className' : 'bg-primary',
            'description': f"Teacher: {tt.teacher}"
        })

    context = {
        'timetable_list' : timeTables,
        'events_json' : json.dumps(events)
    }


    return render(request, 'management/time-table.html', context)

@login_required(login_url='login')
def teacher_timetable(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("Accès refusé.")
        
    # Récupérer le profil du prof et SES cours
    teacher_profile = Teacher.objects.get(user=request.user)
    my_schedule = TimeTable.objects.filter(teacher=teacher_profile)
    
    # Préparer les données pour FullCalendar
    events = []
    for tt in my_schedule:
        start_datetime = f"{tt.date.isoformat()}T{tt.start_time.strftime('%H:%M:%S')}"
        end_datetime = f"{tt.date.isoformat()}T{tt.end_time.strftime('%H:%M:%S')}"
        events.append({
            'title': f"{tt.subject} ({tt.class_name})",
            'start': start_datetime,
            'end': end_datetime,
            'className': 'bg-success', # Couleur verte pour les profs
            'description': f"Classe: {tt.class_name}"
        })

    context = {
        'events_json': json.dumps(events),
        'page_title': 'Mon Emploi du Temps (Enseignant)'
    }
    return render(request, 'teachers/teacher_timetable.html', context)


@login_required(login_url='login')
def student_timetable(request):
    if not request.user.is_student:
        return HttpResponseForbidden("Accès refusé.")
        
    # Récupérer le profil de l'étudiant et les cours de SA classe
    student_profile = Student.objects.get(user=request.user)
    my_class_schedule = TimeTable.objects.filter(class_name=student_profile.student_class)
    
    # Préparer les données pour FullCalendar
    events = []
    for tt in my_class_schedule:
        start_datetime = f"{tt.date.isoformat()}T{tt.start_time.strftime('%H:%M:%S')}"
        end_datetime = f"{tt.date.isoformat()}T{tt.end_time.strftime('%H:%M:%S')}"
        events.append({
            'title': f"{tt.subject}",
            'start': start_datetime,
            'end': end_datetime,
            'className': 'bg-primary', 
            'description': f"Professeur: {tt.teacher.first_name} {tt.teacher.last_name}"
        })

    context = {
        'events_json': json.dumps(events),
        'page_title': 'Mon Emploi du Temps (Étudiant)'
    }
    return render(request, 'students/student_timetable.html', context)

@login_required(login_url='login')
def add_marks(request, exam_id):
    if not request.user.is_teacher:
        return HttpResponseForbidden("Accès refusé.")

    exam = get_object_or_404(Exam, id=exam_id)
    
    students = Student.objects.filter(student_class=exam.exam_class)

    existing_results = Result.objects.filter(exam=exam)
    results_dict = {res.student_id: res for res in existing_results}

    if request.method == 'POST':
        for student in students:
            # Récupérer les données envoyées par les inputs dynamiques
            mark_value = request.POST.get(f"mark_{student.id}")
            comment_value = request.POST.get(f"comment_{student.id}")

            if mark_value: 
                Result.objects.update_or_create(
                    student=student,
                    exam=exam,
                    defaults={'marks': mark_value, 'comments': comment_value}
                )
        
        messages.success(request, "Les notes ont été enregistrées avec succès !")
        return redirect('exam')

    student_data = []
    for student in students:
        res = results_dict.get(student.id)
        student_data.append({
            'student': student,
            'mark': res.marks if res else '',
            'comment': res.comments if res else ''
        })

    context = {
        'exam': exam,
        'student_data': student_data,
    }
    return render(request, 'management/add_marks.html', context)

@login_required(login_url='login')
def add_holiday(request):
    if not request.user.is_admin:
        return HttpResponseForbidden("Accès refusé. Réservé aux administrateurs.")
        
    if request.method == 'POST':
        name = request.POST.get('name')
        holiday_type = request.POST.get('holiday_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description = request.POST.get('description')
        
        Holiday.objects.create(
            name=name, holiday_type=holiday_type,
            start_date=start_date, end_date=end_date, description=description
        )
        messages.success(request, "Jour férié ajouté avec succès !")
        return redirect('admin_dashboard') 

    return render(request, 'management/add_holiday.html')


@login_required(login_url='login')
def add_timetable(request):
    if not request.user.is_admin:
        return HttpResponseForbidden("Accès refusé. Réservé aux administrateurs.")
    
    teachers = Teacher.objects.all()
    
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        subject = request.POST.get('subject')
        teacher_id = request.POST.get('teacher_id')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        teacher = get_object_or_404(Teacher, id=teacher_id)
        
        TimeTable.objects.create(
            class_name=class_name, subject=subject, teacher=teacher,
            date=date, start_time=start_time, end_time=end_time
        )
        messages.success(request, "Cours ajouté à l'emploi du temps avec succès !")
        return redirect('admin_dashboard') 
        
    return render(request, 'management/add_timetable.html', {'teachers': teachers})

@login_required(login_url='login')
def add_exam(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("Accès refusé. Réservé aux enseignants.")
    
    teacher_profile = Teacher.objects.get(user=request.user)
    my_subjects = Subject.objects.filter(teacher=teacher_profile)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        exam_class = request.POST.get('exam_class')
        subject_name = request.POST.get('subject') 
        exam_date = request.POST.get('exam_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        
        Exam.objects.create(
            name=name, exam_class=exam_class, subject=subject_name,
            exam_date=exam_date, start_time=start_time, end_time=end_time
        )
        messages.success(request, "Examen programmé avec succès !")
        return redirect('exam')
        
    return render(request, 'management/add_exam.html', {'my_subjects': my_subjects})