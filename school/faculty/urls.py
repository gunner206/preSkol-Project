#faculty/urls.py

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('holiday/', views.holiday, name='holiday'),
    path('exam/', views.exam, name='exam'),
    path('time_table/', views.time_table, name='time_table'),
]