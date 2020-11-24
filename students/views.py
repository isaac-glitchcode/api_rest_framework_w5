from django.shortcuts import render
from django.http import HttpResponse
from students.models import Student


def home(req):
    return render(req, 'index/index.html', {})

def get_students(req):
    students = Student.objects.all()
    context = {
        'students': students 
    }
    return render(req, 'students/index.html', context)

def get_student(req, id):
    student = Student.objects.get(id=id)
    classes = student.classes.all()
    context = {
        'student': student,
        'classes': classes,
    }
    return render(req, 'students/student_single.html', context)