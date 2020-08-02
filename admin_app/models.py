from django.db import models
from django.contrib.auth.models import AbstractUser



class courses(models.Model):
    course_name = models.CharField(max_length=50, default=None, null=True)
    course_fees = models.CharField(max_length=50, default=None, null=True)
    course_detail = models.CharField(max_length=200, default=None, null=True)


    def __str__(self):
        return self.course_name


class user_registration(AbstractUser):
    dob = models.CharField(max_length=10, default=None, null=True)
    contact = models.CharField(max_length=10, default=None, null=True)
    course_name = models.ForeignKey(courses, on_delete=models.CASCADE, default=None, null=True)
    address = models.TextField(max_length=200, default=None, null=True)
    user_type = models.CharField(max_length=20, default= None, null=True, choices=(('admins','admins'),('teacher','teacher'),('student','student')))
    designation = models.CharField(max_length=20, default= None, null=True, choices=(('manager','manager'),('principal','principal')))
    images=models.URLField(null=True, default=None)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
