from django.shortcuts import render, redirect
from admin_app.models import user_registration, classes
from pages.views import students_view



def stuent_registration_view(request):
    if request.method == 'POST' : 
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        class_name = request.POST['class_name']
                
        user_registration.objects.create_user(first_name=first_name, last_name=last_name, dob=dob, 
                                                         email=email, contact=contact, address=address, 
                                                         username=email, password=password, user_type='student',
                                                         class_name=classes.objects.get(class_name=class_name), subject_name=None)                                                               

        return redirect(students_view)
    else:        
        return render(request, 'student_registration.html')

