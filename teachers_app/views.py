from django.shortcuts import render, redirect
from admin_app.models import courses, user_registration
from pages.views import teachers_view, admin_dashboard_index_view
from pages.views import teacher_dashboard_view
from django.conf import settings
from django.core.files.storage import FileSystemStorage





def add_new_teacher_view(request):
    if request.method == 'POST' and request.FILES['h_image']:
        myfile=request.FILES['h_image']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        imgurl=fs.url(filename)

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['birthdate']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        course_select = request.POST['course_select']
        image=imgurl
        
        
        user_registration.objects.create_user(first_name=first_name, last_name=last_name, dob=dob, 
                                                         email=email, contact=contact, address=address, 
                                                         username=email, password=contact, user_type='teacher',
                                                         course_name=courses.objects.get(course_name=course_select),
                                                         images=image)        

        return redirect(teachers_view)
    else:
        course_list = courses.objects.all()
        return render(request, 'add_new_teacher.html', {'course_list': course_list})





