# home_auth/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST.get('role') # student, teacher ou admin

        # Créer l'utilisateur
        user = CustomUser.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        # Assigner le rôle
        if role == 'student':
            user.is_student = True
        elif role == 'teacher':
            user.is_teacher = True
        elif role == 'admin':
            user.is_admin = True
        
        user.save()
        login(request, user)
        messages.success(request, 'Signup successful!')
        return redirect('index')
    
    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        # Using .get() prevents dictionary crash if the form inputs are named differently
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        print(f"--- DEBUG: Attempting login for email: {email} ---")
        
        # Django uses 'username' keyword, which is mapped to email in your DB
        user = authenticate(request, username=email, password=password)
        
        print(f"--- DEBUG: Authenticate returned: {user} ---")
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            
            print(f"--- DEBUG: Roles -> Admin:{user.is_admin}, Teacher:{user.is_teacher}, Student:{user.is_student} ---")

            if user.is_admin:
                return redirect('admin_dashboard')
            elif user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('student_dashboard') 
            else:
                messages.error(request, 'Invalid user role')
                return redirect('index')
        else:
            print("--- DEBUG: Authentication failed! Returning to login page. ---")
            messages.error(request, 'Invalid credentials')
            return render(request, 'authentication/login.html')
            
    return render(request, 'authentication/login.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')

def forgot_password_view(request):
    return redirect(request, 'authentication/forgot-password.html')

@login_required(login_url='login') # Redirects to login if not authenticated
def admin_dashboard(request):
    if not request.user.is_admin:
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    # Pass specific data for the admin here
    return render(request, 'Home/admin-dashboard.html')

@login_required(login_url='login')
def teacher_dashboard(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("You are not authorized to view this page.")
        
    # Pass specific data for the teacher here
    return render(request, 'teachers/teacher-dashboard.html')

@login_required(login_url='login')
def student_dashboard(request):
    if not request.user.is_student:
        return HttpResponseForbidden("You are not authorized to view this page.")
        
    # Pass specific data for the student here
    return render(request, 'students/student-dashboard.html')