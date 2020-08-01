from django.shortcuts import render, redirect
from .models import courses, user_registration
from pages.views import admin_dashboard_tables_view, teachers_view, teacher_dashboard_view, admin_dashboard_index_view, student_dashboard_view, webiste_index_view
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login, logout, authenticate


def add_course_view(request):
    if request.method == 'POST':
        course_name = request.POST['add_course_name']
        course_fees = request.POST['add_course_fees']
        course_detail = request.POST['add_course_detail']
        new_course = courses(course_name=course_name, course_fees=course_fees, course_detail=course_detail)
        new_course.save()
        return redirect(admin_dashboard_tables_view)
    else:
        return render(request, 'admin_dashboard_tables.html')


def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        User = authenticate(request, username=uname, password=password)
        if User is not None:
            login(request, User)
            if User.user_type == 'teacher':                
                return redirect(teacher_dashboard_view)
            elif User.user_type == 'admins':
                return redirect(admin_dashboard_index_view)
            elif User.user_type == 'student':
                return redirect(student_dashboard_view)
            else:                
                return render(request, 'website_login.html')                 
        else:
            return render(request, 'website_login.html')
    else:
        return render(request, 'website_login.html')




def logout_view(request):
    logout(request)
    return redirect(webiste_index_view)