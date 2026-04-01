from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('teacher-details/<int:teacher_id>/', views.teacher_view, name='teacher_view'),
    path('edit-teacher/<int:teacher_id>/', views.teacher_edit, name='teacher_edit'),
    path('delete-teacher/<int:teacher_id>/', views.teacher_delete, name='teacher_delete'),
]