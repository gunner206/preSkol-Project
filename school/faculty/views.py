from django.shortcuts import render
from django.http import HttpResponse
from .models import Holiday, Exam, TimeTable
import json

# Create your views here.
def index(request):
    return render(request, 'authentication/login.html')

def dashboard(request):
    return render(request, 'students/student-dashboard.html')

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

