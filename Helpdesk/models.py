from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    course = models.CharField(max_length=50)


class StudentCourse(models.Model):
    title = models.CharField(max_length=150)
    full_form = models.CharField(max_length=150)
    desc = models.TextField()
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    course_fees = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class StudentSyllabus(models.Model):
    title = models.CharField(max_length=150)
    my_file = models.FileField(upload_to='syllabus', blank=True)

    def __str__(self):
        return self.title