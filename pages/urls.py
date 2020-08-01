from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # =========== Start Webiste URL Content ============

    path('admin_dashboard',views.admin_dashboard_index_view,name='admin_dashboard'),
    path('admin_dashboard_tables',views.admin_dashboard_tables_view,name='admin_dashboard_tables'),
    path('teachers',views.teachers_view,name='teachers'),
    path('teacher_dashboard',views.teacher_dashboard_view,name='teacher_dashboard'),
    path('students',views.students_view,name='students'),    
    path('student_dashboard',views.student_dashboard_view,name='student_dashboard'),
    path('about',views.website_about_view,name='about'),
    path('courses',views.website_course_view,name='courses'),
    path('course_detail',views.website_course_detail_view,name='course_detail'),
    path('blog',views.website_blog_view,name='blog'),
    path('contact',views.website_contact_view,name='contact'),
    path('student_registration',views.student_registration_view,name='student_registration'),













    # =========== End Webiste URL Content ============



    # =========== Start Webiste URL Content ============

    path('',views.webiste_index_view,name='website_index'),





    # =========== End Webiste URL Content ============






]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)