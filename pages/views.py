from django.shortcuts import render, redirect
from admin_app.models import courses, user_registration



def admin_dashboard_index_view(request):
    return render(request, 'admin_dashboard_index.html')

def admin_dashboard_tables_view(request):
    course_list = courses.objects.all()
    return render(request, 'admin_dashboard_tables.html', {'course_list': course_list})

def teachers_view(request):
    teachers_list = user_registration.objects.filter(user_type='teacher')
    join_date = user_registration.objects.all()
    return render(request, 'teachers.html', {'teachers_list':teachers_list, 'join_date':join_date})

def teacher_dashboard_view(request):
    return render(request, 'teacher_dashboard.html')

def students_view(request):
    students_list = user_registration.objects.filter(user_type='student')
    return render(request, 'admin_dashboard_student.html', {'student_list':students_list})

def student_dashboard_view(request):
    return render(request, 'student_dashboard.html')










# =========== Start Webiste Function Content ============


def webiste_index_view(request):
    course_list = courses.objects.all()
    teachers_list = user_registration.objects.filter(user_type='teacher')
    return render(request, 'website_index.html', {'course_list':course_list, 'teachers_list':teachers_list})


def website_about_view(request):
    return render(request, 'website_about.html')

def website_course_view(request):
    course_list = courses.objects.all()
    return render(request, 'courses.html', {'course_list':course_list})

def website_course_detail_view(request):
    return render(request, 'course_details.html')

def website_blog_view(request):
    return render(request, 'blog.html')

def website_contact_view(request):
    return render(request, 'contact.html')

def student_registration_view(request):
    return render(request, 'student_registration.html')





# =========== End Webiste Function Content ============