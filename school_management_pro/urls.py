from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('',include('admin_app.urls')),
    path('',include('teachers_app.urls')),
    path('',include('student_app.urls')),



]
