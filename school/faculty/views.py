from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from .models import Holiday, Exam, TimeTable, Result
from teacher.models import Teacher
from student.models import Student
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
            'className': 'bg-primary', # Couleur bleue pour les étudiants
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
    
    # Récupérer tous les étudiants inscrits dans la classe de cet examen
    students = Student.objects.filter(student_class=exam.exam_class)

    # Récupérer les notes existantes pour pré-remplir le formulaire (si le prof modifie)
    existing_results = Result.objects.filter(exam=exam)
    results_dict = {res.student_id: res for res in existing_results}

    # Traitement de la sauvegarde des notes
    if request.method == 'POST':
        for student in students:
            # Récupérer les données envoyées par les inputs dynamiques
            mark_value = request.POST.get(f"mark_{student.id}")
            comment_value = request.POST.get(f"comment_{student.id}")

            if mark_value: # Si une note a été saisie
                # Met à jour la note si elle existe, sinon la crée
                Result.objects.update_or_create(
                    student=student,
                    exam=exam,
                    defaults={'marks': mark_value, 'comments': comment_value}
                )
        
        messages.success(request, "Les notes ont été enregistrées avec succès !")
        return redirect('exam')

    # Préparer les données pour le template (fusionner l'étudiant et sa note existante)
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